%%%��plot���ģ�
clc
clear all
close all;
%�������������

x1=-3:0.01:0;
x2=0:0.01:3;
hn=figure('name','2020���˽ڿ���','MenuBar','None');
set(hn,'color','w');

for t=1:50
cla

eval('yleft=(-x1).^(2/3)+(0.9*(3.3-(-x1).^2).^0.5).*sin(t*pi*(-x1)) ');

eval('yright=x2.^(2/3)+(0.9*(3.3-x2.^2).^0.5).*sin(t*pi*x2) ');
%eval��������ֱ�Ӱ��ַ�����������ִ�У�ֱ�������ߺ������ұߺ�����ֵ

plot(x1,yleft,'*r',x2,yright,'*r');
axis([-1.8 1.8 -1.5 2.5]);
axis off; %ȥ������

pause(0.01); %����ͣ�γɶ���Ч��
title('2020���˽ڿ��֣�����'); %ˢ��

end
clc;