import cv2

# Učitajte videozapis
video = cv2.VideoCapture('traffic2.mp4')

# Stvorite objekt za detekciju prednjeg plana
mog = cv2.createBackgroundSubtractorMOG2()

# Definirajte prag detekcije prednjeg plana
foreground_threshold = 50

# Prolazak kroz sve frejmove u videu
while True:
    # Čitajte sljedeći frejm
    ret, frame = video.read()
    
    if not ret:
        break
    
    # Primijenite detektor prednjeg plana na frejm
    foreground_mask = mog.apply(frame)
    
    # Uklonite šum iz detekcije prednjeg plana
    foreground_mask = cv2.medianBlur(foreground_mask, 5)
    
    # Primijenite prag detekcije prednjeg plana
    foreground_mask[foreground_mask < foreground_threshold] = 0
    
    # Primijenite morfološke operacije za uklanjanje šuma i povećanje kontura
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, kernel)
    foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_CLOSE, kernel)
    
    # Identificirajte konture u detekciji prednjeg plana
    contours, _ = cv2.findContours(foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Uklonite konture koje predstavljaju vozila
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), -1)
    
    # Prikazite izlazni frejm
    cv2.imshow('Izlaz', frame)
    
    # Provjerite pritisak na tipku ESC
    if cv2.waitKey(1) == 27:
        break

# Oslobodite resurse
video.release()
cv2.destroyAllWindows()
