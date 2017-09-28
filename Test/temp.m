%% Ambarella_Large
I = imread('3.jpg');
H = rgb2hsv(I);
Hue=H;
Hue(:,:,2:3) = 0;

V=H;
V(:,:,1:2) = 0;
subplot(131);
imshow(Hue);
title('H');
subplot(132);
imshow(H(:,:,2));

title('S');
BW = H(:,:,2);
wname = 'sym4';
[CA,CH,CV,CD] = dwt2(BW,wname,'mode','per');
subplot(221)
imagesc(CA)
title('CA')
colormap gray
subplot(222)
imagesc(CH)
title('CH')
subplot(223)
imagesc(CV)
title('CV')
subplot(224)
imagesc(CD)
title('CD')
