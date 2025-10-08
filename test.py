import cv2

# Ouvre la caméra (0 = webcam par défaut)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d’ouvrir la caméra.")
    exit()

while True:
    # Capture une frame
    ret, frame = cap.read()
    
    if not ret:
        print("Erreur : Impossible de lire la vidéo.")
        break

    # Affiche l'image
    cv2.imshow("Retour caméra", frame)

    # Quitte si on appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère la caméra et ferme la fenêtre
cap.release()
cv2.destroyAllWindows()
