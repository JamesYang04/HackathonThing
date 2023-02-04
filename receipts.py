import cv2
import pytesseract
import openai
import config

openai.api_key = config.api_key

# image = cv2.imread("walmart-receipt.jpeg")

cam = cv2.VideoCapture(0)
cv2.namedWindow("Test")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: failed to grab frame.")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Closing camera...")
        break

    if k%256 == 32:
        img_name = "receipt{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{}written!".format(img_name))
        img_counter += 1
        break

cam.release()
cv2.destroyAllWindows()

image = cv2.imread("receipt0.png")
# Pre-processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

gray = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
# OCR
text = pytesseract.image_to_string(gray)

prompt = f"Extract only the grocery items from the following text, remove all numbers: {text}"
# lines = text.split("\n")

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

grocery_items = response["choices"][0]["text"].strip().split(", ")

print("Grocery items:")
for item in grocery_items:
    item = item.lower()
    print(item)