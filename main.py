from skimage.metrics import structural_similarity as ssim
import cv2
import csv
import timeit

# Function to compare images
def compare_images(imageA, imageB):
    # Convert images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Compare both images and retrieve SSIM
    score = ssim(grayA, grayB)
    return score

#Function to write output csv using output array
def write_csv(output_array):
    # Creates new output.csv
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Writes the header row
        writer.writerow(["image1", "image2", "similar", "elapsed"])
        # Prints output array into csv
        writer.writerows(output_array)


# Opens csv and reads the file
with open('images.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    output_array = []
    for row in csv_reader:
        if line_count == 0:
            # Ignores header row
            print(f'Column name are {", ".join(row)}')
            line_count +=1
        else:
            # Takes image filenames from row and scans images folder for the image
            imageA = cv2.imread(f'images/{row[0]}')
            imageB = cv2.imread(f'images/{row[1]}')
            line_count += 1

            # Starts timer and calls the compare_images function to retrieve SSIM
            start = timeit.default_timer()
            score = round(compare_images(imageA, imageB),2)
            stop = timeit.default_timer()
            print(f'{row[0]} vs {row[1]}: SSIM: {abs(score - 1)}, elapsed {round(stop - start, 2)}')
            # Adds values to output_array
            output_array.append([row[0], row[1], abs(score - 1), round(stop - start, 2)])
            
        print(f'Processed {line_count} lines.')
    # Calls write_csv function to write output csv using output Array
    write_csv(output_array)


