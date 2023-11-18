import os
import cv2



def write_txt(folder, img, objects, top_left, bottom_right, save_dir):
   
    cls = int(input("Enter class"))
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape
   
    box_height=(bottom_right[0][0]-top_left[0][0])/height
    box_width=(bottom_right[0][1]-top_left[0][1])/width
    centre_x=((bottom_right[0][0]+top_left[0][0])/2)/width
    centre_y=((bottom_right[0][1]+top_left[0][1])/2)/height
    
    values=[cls,centre_x,centre_y,box_width,box_height]
    line_to_write = ",".join(map(str, values))
    filename=img.name
    image_base_name = os.path.splitext(os.path.basename(filename))[0]
    txt_file_name = f"{image_base_name}.txt"
    with open(txt_file_name, "w") as file:
       file.write(line_to_write)
    
    
    
    

if __name__ == '__main__':
    folder = 'images'
    img = [im for im in os.scandir('images')]
    objects = ['vortex_center']
    top_left = [(12, 56)]
    bottom_right = [(45, 14)]
    save_dir = 'annotation'
    write_txt(folder, img, objects, top_left, bottom_right, save_dir)
