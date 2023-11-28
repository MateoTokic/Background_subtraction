import cv2
import skfuzzy as fuzz

import numpy as np

# Učitavanje videa
cap = cv2.VideoCapture('traffic2.mp4')

# Definiranje funkcije za stvaranje Fuzzy modela
def create_fuzzy_model():
    # Definiranje ulaznih varijabli
    x = np.arange(0, 256, 1)
    invar_dark = fuzz.trapmf(x, [0, 0, 50, 100])
    invar_bright = fuzz.trapmf(x, [150, 200, 256, 256])
    # Definiranje izlazne varijable
    outvar = np.arange(0, 256, 1)
    outvar_auto = fuzz.trapmf(outvar, [0, 0, 60, 120])
    # Definiranje pravila
    rule1 = fuzz.relation_min(invar_dark, outvar_auto)
    rule2 = fuzz.relation_min(invar_bright, outvar_auto)
    # Stvaranje Fuzzy modela
    model = fuzz.control.ControlSystem([rule1, rule2])
    return model

# Definiranje funkcije za obradu slike Fuzzy modelom
def process_image(image, model):
    # Konvertiranje slike u grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Primjena Fuzzy modela na grayscale sliku
    result = fuzz.defuzz(out_var='outvar', aggregated=gray, rules=model)

    # Pretvorba izlaza u binarnu sliku
    threshold = cv2.threshold(result.astype(np.uint8), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Pronalaženje kontura
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Uklanjanje kontura koje su manje od 100 piksela
    contours = [contour for contour in contours if cv2.contourArea(contour) > 100]

    # Crtanje kontura na originalnoj slici
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    return image

# Stvaranje Fuzzy modela
model = create_fuzzy_model()

# Petlja za obradu video zapisa
while True:
    # Učitavanje slike iz videa
    ret, frame = cap.read()

    # Prekidanje petlje ako nema više slika
    if not ret:
        break

    # Obrada slike Fuzzy modelom
    processed_frame = process_image(frame, model)

    # Prikazivanje obradene slike
    cv2.imshow('frame', processed_frame)

    # Prekidanje petlje pritiskom na 'q' tipku
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Oslobađanje resursa
cap.release()
cv2.destroyAllWindows()
