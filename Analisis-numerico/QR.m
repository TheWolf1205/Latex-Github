format rational
A=[4,1,-2,2;1,2,0,1;-2,0,3,-2;2,1,-2,-1]
x1=A(:,1);
e1=sqrt((x1'*x1))*eye(4,1);
u1=x1-e1;
v1 = u1/sqrt((u1'*u1));
Q1=eye(4)-2*(v1*v1');
A2=Q1*A;


SA2=A2(2:4,2:4);
x2= SA2(:,1);
e2=sqrt((x2'*x2))*eye(3,1);
u2=x2-e2;
v2=u2/sqrt((u2'*u2));
SubQ2=eye(3)-2*(v2*v2');
Q2=zeros(4,4);
Q2(1,1)=1;
Q2(2:4,2:4)=SubQ2;
A3=Q2*A2;

SA3=A3(3:4,3:4);
x3= SA3(:,1);
e3=sqrt((x3'*x3))*eye(2,1);
u3=x3-e3;
v3=u3/sqrt((u3'*u3));
SubQ3=eye(2)-2*(v3*v3');
Q3=zeros(4,4);
Q3(1,1)=1;
Q3(2,2)=1;
Q3(3:4,3:4)=SubQ3;
A4=Q3*A3;

Q=Q1*Q2*Q3
R=A4

QR=Q*R