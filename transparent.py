import cv2
import os

def transparent(img):
    # 画像の読み込み
    img = cv2.imread(img)
    # 画像のサイズ
    height, width = img.shape[:2]
    # 画像の白い部分を透過する
    for i in range(height):
        for j in range(width):
            if img[i, j][0] == 255 and img[i, j][1] == 255 and img[i, j][2] == 255:
                img[i, j][3] = 0
    return img

if __name__ == '__main__':
    # 画像のフォルダ
    folder = 'img'
    # 画像のファイル名(.DS_Storeを除く)
    img_name = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f != '.DS_Store']
    for i in img_name:
        print(folder + '/' + i)
        img = transparent(folder + '/' + i)
        # 画像の保存
        cv2.imwrite(folder + '/' + i, img)

