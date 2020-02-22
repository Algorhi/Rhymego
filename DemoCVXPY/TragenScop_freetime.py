# -* coding: utf-8 -*-
"""
Created on Fri Dec 1 00:36:49 2017

@author: JiangHaven 
"""

import numpy as np
import cvxpy as cvx
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
print('TragenScop','\n','--Trajectory Generation Using Sequance Convex Optimization Programming') 
x0,y0,z0 = 0,0,0
xf,yf,zf = 400,400,400
psi0,phi0 = 20*np.pi/180,40*np.pi/180
psif,phif = 40*np.pi/180,80*np.pi/180
Vconst = 10;rate_max = 5*np.pi/180
Vx0 = Vconst*np.sin(psi0);Vxf=Vconst*np.sin(psif)
Vy0 = Vconst*np.cos(psi0)*np.sin(phi0);Vyf=Vconst*np.cos(psif)*np.sin(phif)
Vz0 = Vconst*np.cos(psi0)*np.cos(phi0);Vzf=Vconst*np.cos(psif)*np.cos(phif)
N = 100;tau = 0.21#tau = 0.188
S = 5
S = S+1
Xobs = 200;Yobs = 210;Zobs = 90;R = 20;flag_az = 1
time = np.linspace(1,N,N-1)*tau
Xk= np.zeros([S,N])
Yk= np.zeros([S,N])
Zk= np.zeros([S,N])
Xk_temp= np.zeros([N])
Yk_temp= np.zeros([N])
Zk_temp= np.zeros([N])
Xk[0,:] = np.linspace(x0,xf,N)
Yk[0,:] = np.linspace(y0,yf,N)
Zk[0,:] = np.linspace(z0,zf,N)
V_=np.zeros([N-1,])
for s in range(S-1):
     Xk_temp = Xk[s,:];Yk_temp = Yk[s,:];Zk_temp= Zk[s,:]#
     fobs=[np.linalg.norm([Xk_temp[i] - Xobs,Yk_temp[i] - Yobs,Zk_temp[i] - Zobs])**2
     -R**2 for i in range(len(Zk_temp))]
     fobs=np.array(fobs)
     #define state and control variables
     T = cvx.Variable(1,1)
     x = cvx.Variable(1,N)
     y = cvx.Variable(1,N)
     z = cvx.Variable(1,N)
     Vx= cvx.Variable(1,N-1)
     Vy= cvx.Variable(1,N-1)
     Vz= cvx.Variable(1,N-1)
     VV= cvx.Variable(3,N-1);
     u1 = cvx.Variable(1,N-2)
     u2 = cvx.Variable(1,N-2)
     u3 = cvx.Variable(1,N-2)
     UU = cvx.Variable(3,N-2)
     #state constrants
     F   =  [0 <= T]    
     F  += [x[0,0]   == x0]
     F  += [x[0,N-1] == xf]
     F  += [y[0,0]   == y0]
     F  += [y[0,N-1] == yf]
     F  += [z[0,0]   == z0]
     F  += [z[0,N-1] == zf]
#     F  += [x0 <= x,x <= xf]
#     F  += [y0 <= y,y <= yf]
#     F  += [z0 <= z,z <= zf]
     #angle init constrants
     F  += [Vx[0,0]==Vx0*T]
     F  += [Vy[0,0]==Vy0*T]
     F  += [Vz[0,0]==Vz0*T]
     #angle terminal constrants
     F  += [Vx[0,N-2]==Vxf*T]
     F  += [Vy[0,N-2]==Vyf*T]
     F  += [Vz[0,N-2]==Vzf*T]
     #angle constrants
#     F  += [-10*Vconst<=u1,u1<= 10*Vconst]
#     F  += [-10*Vconst<=u2,u2<= 10*Vconst]
#     F  += [-10*Vconst<=u3,u3<= 10*Vconst]
     # Cone Constraints
     F  += [Vx[0,i]==VV[0,i] for i in range(N-1)] 
     F  += [Vy[0,i]==VV[1,i] for i in range(N-1)] 
     F  += [Vz[0,i]==VV[2,i] for i in range(N-1)]    
     F  += [u1[0,i]==UU[0,i] for i in range(N-2)] 
     F  += [u2[0,i]==UU[1,i] for i in range(N-2)] 
     F  += [u3[0,i]==UU[2,i] for i in range(N-2)]      
     F  += [cvx.norm(VV[:,i])<=T*Vconst for i in range(N-1)]
     F  += [cvx.norm(UU[:,i])<=T*rate_max*Vconst for i in range(N-2)]
 

     
     # Dynamic constraints    
     F  += [x[0,i+1] == x[0,i] + tau*Vx[0,i] for i in range(N-1)]
     F  += [y[0,i+1] == y[0,i] + tau*Vy[0,i] for i in range(N-1)]
     F  += [z[0,i+1] == z[0,i] + tau*Vz[0,i] for i in range(N-1)]
     F  += [Vx[0,i+1] == Vx[0,i] + tau*u1[0,i] for i in range(N-2)]
     F  += [Vy[0,i+1] == Vy[0,i] + tau*u2[0,i] for i in range(N-2)]
     F  += [Vz[0,i+1] == Vz[0,i] + tau*u3[0,i] for i in range(N-2)]     
     #Sequence Avidance Zones constraints
#     if flag_az == 1:
     F  += [-(fobs[ii]+2*(Xk_temp[ii]-Xobs)*(x[0,ii]-Xk_temp[ii])+2*(Yk_temp[ii]-
     Yobs)*(y[0,ii]-Yk_temp[ii])+2*(Zk_temp[ii]-Zobs)*(z[0,ii]-Zk_temp[ii]))<=0 
     for ii in range(N)]
     #Sequence angle rate constraints
#     F  += [(fobs[ii]+2*(Xk_temp[ii]-Xobs)*(x[0,ii]-Xk_temp[ii])+2*(Yk_temp[ii]-
#     Yobs)*(y[0,ii]-Yk_temp[ii])+2*(Zk_temp[ii]-Zobs)*(z[0,ii]-Zk_temp[ii]))>=0
#            for ii in range(N)]
#     F  += [(fobs[ii]+2*(Xk_temp[ii]-Xobs)*(x[0,ii]-Xk_temp[ii])+2*(Yk_temp[ii]-
#     Yobs)*(y[0,ii]-Yk_temp[ii])+2*(Zk_temp[ii]-Zobs)*(z[0,ii]-Zk_temp[ii]))>=0
#            for ii in range(N)]     
     #Set optimal objective
     obj = cvx.Minimize(T)     
     prob = cvx.Problem(obj, F)
     prob.solve(solver='ECOS')#CVXOPT SCS 默认的是ECOS
#     result = prob.solve()
     if x.value is None:
         print('Optimization probem is infeasibale! Please cheak the inital parameters settings')
         X=np.zeros([1,N])
         Y=X
         Z=X
     else:
         print('TragenScop completed' ,s, 'times optimization')         
         X=x.value.A.flatten();Y=y.value.A.flatten();Z=z.value.A.flatten()
         VX=Vx.value.A.flatten();VY=Vy.value.A.flatten();VZ=Vz.value.A.flatten()
         U1=u1.value.A.flatten();U2=u2.value.A.flatten();U3=u3.value.A.flatten()
         TT=T.value
         Xk[s+1,:] = X; Yk[s+1,:] = Y; Zk[s+1,:] = Z
         if s == S-2:
             fig1 = plt.figure(1)
             ax = Axes3D(fig1)
             ax.plot(X,Y,Z)
         V_=np.sqrt(VX**2+VY**2+VZ**2)/TT
         rate=np.sqrt(U1**2+U2**2+U3**2)/(TT*Vconst)
         fig2 = plt.figure(2)
         plt.plot(time*TT,VX,'g.-',time*TT,VY,'b.-',time*TT,VZ,'r.-',time*TT,V_,'k.-')
         plt.plot(time*TT,V_)
         fig3 = plt.figure(3)
         plt.plot(time[0:N-2]*TT,rate*180/np.pi)

