%%�����Ǻ���
function shili02
h0=figure('toolbar','none',...  %���ù�����
    'position',[200 150 450 350],...  %����ͼ���С
    'name','ʵ��02');  %������
x=-pi:0.05:pi;  %x�ķ�Χ
y=sin(x)+cos(x);  %����
plot(x,y,'-*r','linewidth',1);  %��ͼ
grid on  %����
xlabel('�Ա���X');  %x��������
ylabel('����ֵY');  %y��������
title('���Ǻ���');  %����

imin=find(min(y)==y);
imax=find(max(y)==y);
text(x(imin),y(imin),...
    ['\leftarrow��Сֵ=',num2str(y(imin))],...
    'fontsize',16)
text(x(imax),y(imax),...
    ['\leftarrow���ֵ=',num2str(y(imax))],...
    'fontsize',16)