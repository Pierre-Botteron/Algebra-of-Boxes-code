#import numpy as np
import torch

#
#   WIRINGS
#

def functions_to_wiring(f1, g1, f2, g2, f3, g3):
    # the fi and gj are tensors
    W = torch.zeros(32)
    for x in range(2):
        for a in range(2):
            W[2*x+a] = f1[x,a]
            W[2*x+a+4] = g1[x,a]
            W[2*x+a+8] = f2[x,a]
            W[2*x+a+12] = g2[x,a]
            for a2 in range(2):
                W[4*x+2*a+a2+16] = f3[x,a,a2]
                W[4*x+2*a+a2+24] = g3[x,a,a2]
    return W


def W_FWW09(n):  # n is the number of columns
    f1 = torch.zeros((2,2))
    g1 = torch.zeros((2,2))
    f2 = torch.zeros((2,2))
    g2 = torch.zeros((2,2))
    f3 = torch.zeros((2,2,2))
    g3 = torch.zeros((2,2,2))

    for x in range(2):
        for a in range(2):
            f1[x,a] = x
            g1[x,a] = x
            f2[x,a] = x
            g2[x,a] = x
            for a2 in range(2):
                f3[x,a,a2] = (a+a2)%2
                g3[x,a,a2] = (a+a2)%2

    W = functions_to_wiring(f1, g1, f2, g2, f3, g3)
    W.requires_grad = True
    return torch.t(W.repeat(n, 1))

def W_BS09(n):  # n is the number of columns
    W = torch.tensor([0., 0., 1., 1.,              # f_1(x, a_2) = x
            0., 0., 1., 1.,              # g_1(y, b_2) = y
            0., 0., 0., 1.,              # f_2(x, a_1) = a_1*x
            0., 0., 0., 1.,              # g_2(y, b_1) = b_1*y
            0., 1., 1., 0., 0., 1., 1., 0.,  # f_3(x, a_1, a_2) = a_1 + a_2 mod 2
            0., 1., 1., 0., 0., 1., 1., 0.   # g_3(y, b_1, b_2) = b_1 + b_2 mod 2
            ], requires_grad=True)
    return torch.t(W.repeat(n, 1))

def W9(n):  # n is the number of columns
    W = torch.tensor([0.,1.,1.,0.,0.,0.,1.,0.,0.,0.,1.,1.,0.,0.,1.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.], requires_grad=True)
    return torch.t(W.repeat(n, 1))

def W_ABLPSV09a(n):  # n is the number of columns
    f1 = torch.zeros((2,2))
    g1 = torch.zeros((2,2))
    f2 = torch.zeros((2,2))
    g2 = torch.zeros((2,2))
    f3 = torch.zeros((2,2,2))
    g3 = torch.zeros((2,2,2))

    for x in range(2):
        for a in range(2):
            f1[x,a] = x
            g1[x,a] = x
            f2[x,a] = (x+a+1)%2
            g2[x,a] = x*a
            for a2 in range(2):
                f3[x,a,a2] = (a+a2+1)%2
                g3[x,a,a2] = (a+a2+1)%2

    W = functions_to_wiring(f1, g1, f2, g2, f3, g3)
    W.requires_grad = True
    return torch.t(W.repeat(n, 1))

def W_ABLPSV09b(n):  # n is the number of columns
    f1 = torch.zeros((2,2))
    g1 = torch.zeros((2,2))
    f2 = torch.zeros((2,2))
    g2 = torch.zeros((2,2))
    f3 = torch.zeros((2,2,2))
    g3 = torch.zeros((2,2,2))

    for x in range(2):
        for a in range(2):
            f1[x,a] = x
            g1[x,a] = x
            f2[x,a] = x
            g2[x,a] = x
            for a2 in range(2):
                f3[x,a,a2] = a*a2
                g3[x,a,a2] = a*a2

    W = functions_to_wiring(f1, g1, f2, g2, f3, g3)
    W.requires_grad = True
    return torch.t(W.repeat(n, 1))

def W_NSSRRB22(n):  # n is the number of columns
    f1 = torch.zeros((2,2))
    g1 = torch.zeros((2,2))
    f2 = torch.zeros((2,2))
    g2 = torch.zeros((2,2))
    f3 = torch.zeros((2,2,2))
    g3 = torch.zeros((2,2,2))

    for x in range(2):
        for a in range(2):
            f1[x,a] = x
            g1[x,a] = x
            f2[x,a] = x
            g2[x,a] = x
            for a2 in range(2):
                f3[x,a,a2] = max([a,a2])
                g3[x,a,a2] = min([a,a2])

    W = functions_to_wiring(f1, g1, f2, g2, f3, g3)
    W.requires_grad = True
    return torch.t(W.repeat(n, 1))

def W_Pierre_1(n):  # n is the number of columns
    f1 = torch.zeros((2,2))
    g1 = torch.zeros((2,2))
    f2 = torch.zeros((2,2))
    g2 = torch.zeros((2,2))
    f3 = torch.zeros((2,2,2))
    g3 = torch.zeros((2,2,2))

    for x in range(2):
        for a in range(2):
            f1[x,a] = x
            g1[x,a] = x
            f2[x,a] = x
            g2[x,a] = x
            for a2 in range(2):
                f3[x,a,a2] = (a*a2+1)%2
                g3[x,a,a2] = (a*a2+1)%2

    W = functions_to_wiring(f1, g1, f2, g2, f3, g3)
    W.requires_grad = True
    return torch.t(W.repeat(n, 1))

def random_wiring(n):  # n is the number of columns
    return torch.rand((32, n), requires_grad=True)

def random_extremal_wiring(n):  # n is the number of columns
    return torch.randint(2, (32,n))

def wiring_to_functions(W):  # BE CAREFUL!! Here W is a list (with 32 entries)
    # f1
    string0 = "f_1(x,a2) = "
    string = string0
    c = float((W[2]-W[0])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "x"

    c = float((W[1]-W[0])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "a2"

    c = float((W[3]-W[2]-W[1]+W[0])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string += "x·a2"

    c = float((W[0])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "

    print(string)

    # g1
    string0 = "g_1(y,b2) = "
    string = string0
    c = float((W[6]-W[4])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "y"

    c = float((W[5]-W[4])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "b2"

    c = float((W[7]-W[6]-W[5]+W[4])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string += "y·b2"

    c = float((W[4])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "

    print(string)

    # f2
    string0 = "f_2(x,a1) = "
    string = string0
    c = float((W[10]-W[8])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "x"

    c = float((W[9]-W[8])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "a1"

    c = float((W[11]-W[10]-W[9]+W[8])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string += "x·a1"

    c = float((W[8])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "

    print(string)

    # g2
    string0 = "g_2(y,b1) = "
    string = string0
    c = float((W[14]-W[12])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "y"

    c = float((W[13]-W[12])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "b1"

    c = float((W[15]-W[14]-W[13]+W[12])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string += "y·b1"

    c = float((W[12])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "

    print(string)

    # f3
    string0 = "f_3(x,a1,a2) = "
    string = string0
    c = float((W[20]-W[16])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "x"

    c = float((W[18]-W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "a1"

    c = float((W[17]-W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "a2"
    
    c = float((W[21]-W[20]-W[18]+W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "x·a1"
    
    c = float((W[22]-W[20]-W[17]+W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "x·a2"

    c = float((W[19]-W[18]-W[17]+W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "a1·a2"
    
    c = float((W[23] - W[21] - W[22]+W[20] - W[19]+W[18]+W[17] - W[16])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "x·a1·a2"
    
    c = float((W[16])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "
    
    print(string)

    # g3
    string0 = "g_3(y,b1,b2) = "
    string = string0
    c = float((W[28]-W[24])%2)
    if c != 0:
        if c!=1: string+=str(c)+" "
        string+= "y"

    c = float((W[26]-W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "b1"

    c = float((W[25]-W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "b2"
    
    c = float((W[29]-W[28]-W[26]+W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "y·b1"
    
    c = float((W[30]-W[28]-W[25]+W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "y·b2"

    c = float((W[27]-W[26]-W[25]+W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "b1·b2"
    
    c = float((W[31] - W[29] - W[30]+W[28] - W[27]+W[26]+W[25] - W[24])%2)
    if c != 0:
        if string != string0: string+=" ⊕ "
        if c!=1: string+=str(c)+" "
        string+= "y·b1·b2"
    
    c = float((W[24])%2)
    if c !=0:
        if string != string0: string+=" ⊕ "
        string += str(c)+" "
    
    print(string)
    #print("f_1(x,a2) = ", (W[2]-W[0])%2, "x ⊕ ", (W[1]-W[0])%2 ,"a2 ⊕ ", (W[3]-W[2]-W[1]+W[0])%2 ,"x*a2 ⊕ ", (W[0])%2)
    #print("g_1(y,b2) = ", (W[6]-W[4])%2, "y ⊕ ", (W[5]-W[4])%2 ,"b2 ⊕ ", (W[7]-W[6]-W[5]+W[4])%2 ,"y*b2 ⊕ ", (W[4])%2)
    #print("f_2(x,a1) = ", (W[10]-W[8])%2, "x ⊕ ", (W[9]-W[8])%2 ,"a1 ⊕ ", (W[11]-W[10]-W[9]+W[8])%2 ,"x*a1 ⊕ ", (W[8])%2)
    #print("g_2(y,b1) = ", (W[14]-W[12])%2, "y ⊕ ", (W[13]-W[12])%2 ,"b1 ⊕ ", (W[15]-W[14]-W[13]+W[12])%2 ,"y*b1 ⊕ ", (W[12])%2)
    #print("f_3(x,a1,a2) = ", (W[20]-W[16])%2, "x ⊕ ", (W[18]-W[16])%2 ,"a1 ⊕ ", (W[17]-W[16])%2 ,"a2 ⊕ ", 
    #      (W[21]-W[20]-W[18]+W[16])%2 ,"x*a1 ⊕ ", (W[22]-W[20]-W[17]+W[16])%2 ,"x*a2 ⊕ ", 
    #      (W[19]-W[18]-W[17]+W[16])%2 ,"a1*a2 ⊕ ", 
    #      (W[23] - W[21] - W[22]+W[20] - W[19]+W[18]+W[17] - W[16])%2,"x*a1*a2 ⊕ ", (W[16])%2)
    #print("g_3(y,b1,b2) = ", (W[28]-W[24])%2, "y ⊕ ", (W[26]-W[24])%2 ,"b1 ⊕ ", (W[25]-W[24])%2 ,"b2 ⊕ ", 
    #      (W[29]-W[28]-W[26]+W[24])%2 ,"y*b1 ⊕ ", (W[30]-W[28]-W[25]+W[24])%2 ,"y*b2 ⊕ ", 
    #      (W[27]-W[26]-W[25]+W[24])%2 ,"b1*b2 ⊕ ", 
    #      (W[31] - W[29] - W[30]+W[28] - W[27]+W[26]+W[25] - W[24])%2,"y*b1*b2 ⊕ ", (W[16])%2)


def projection_to_extremal_wiring(W): # W is a torch.tensor
    return torch.round(W)



#
#   Link between MATRICES and TENSORS
#

def matrix_to_tensor(Matrix):
    T = torch.reshape(Matrix, (2,2,2,2))
    T = torch.transpose(T, 0, 2)
    T = torch.transpose(T, 1, 3)
    return T

def tensor_to_matrix(Tensor):
    M = torch.transpose(Tensor, 0, 2)
    M = torch.transpose(M, 1, 3)
    return torch.reshape(M, (4,4))




#
#   BOXES
#

def P_L(mu, nu, sigma, tau):
    new_box = torch.zeros((4,4))
    for a in range(2):
        for b in range(2):
            for x in range(2):
                for y in range(2):
                    if a==(mu*x+nu)%2 and b==(sigma*y+tau)%2:
                        new_box[2*x+y, 2*a+b] = 1         
    return new_box


def P_NL(mu, nu, sigma):
    new_box = torch.zeros((4,4))
    for a in range(2):
        for b in range(2):
            for x in range(2):
                for y in range(2):
                    if (a+b)%2==(x*y + mu*x + nu*y + sigma)%2:
                        new_box[2*x+y, 2*a+b] = 0.5               
    return new_box


PR = P_NL(0,0,0)
PRbar = P_NL(0,0,1)
PRprime = P_NL(1,1,1)
P_0 = P_L(0,0,0,0)
P_1 = P_L(0,1,0,1)
SR = (P_0 + P_1)/2
I = 0.25*torch.ones((4,4))
SRbar = 2*I-SR


def corNLB(p):
    return p*PR + (1-p)*SR

                





#
#   CHSH
#

CHSH = torch.zeros((4,4))

for a in range(2):
    for b in range(2):
        for x in range(2):
            for y in range(2):
                if (a+b)%2 == x*y:
                    CHSH[2*x+y, 2*a+b]=0.25

CHSH_flat = matrix_to_tensor( CHSH ).flatten()


CHSH_prime = torch.zeros((4,4))

for a in range(2):
    for b in range(2):
        for x in range(2):
            for y in range(2):
                if (a+b)%2 == ((x+1)%2)*((y+1)%2):
                    CHSH_prime[2*x+y, 2*a+b]=0.25

CHSH_prime_flat = matrix_to_tensor( CHSH_prime ).flatten()

#
#  Which boxes do we test?
#

boxes_above_to_be_tested = [
    (0,0,0,0),
    (0,1,0,1),
    (1,0,1,1),
    (1,1,1,0),
    (0,0,1,0),
    (0,1,1,1),
    (1,0,0,0),
    (1,1,0,1)
    ]

boxes_to_be_tested = [
    (0,0,0,0),
    (0,0,0,1),
    (0,0,1,0),
    (0,0,1,1),
    (0,1,0,0),
    (0,1,0,1),
    (0,1,1,0),
    (0,1,1,1),
    (1,0,0,0),
    (1,0,0,1),
    (1,0,1,0),
    (1,0,1,1),
    (1,1,0,0),
    (1,1,0,1),
    (1,1,1,0),
    (1,1,1,1)
    ]



#
# Known collapsing wirings
#

known_collapsing_W = [
    [0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.],
    [0.,0.,1.,1.,1.,1.,0.,0.,0.,1.,1.,0.,1.,0.,0.,0.,0.,1.,1.,0.,1.,0.,0.,1.,0.,1.,1.,0.,0.,1.,1.,0.],
    [0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,0.,1.,0.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,0.,1.,1.,0.,1.,0.,0.,1.],
    [1.,1.,0.,0.,0.,0.,1.,1.,0.,0.,0.,1.,1.,0.,1.,0.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,0.,1.,1.,0.],
    [0.,0.,1.,1.,1.,1.,0.,0.,0.,0.,1.,0.,1.,0.,0.,1.,1.,0.,0.,1.,0.,1.,1.,0.,1.,0.,0.,1.,1.,0.,0.,1.],
    [1.,1.,0.,0.,1.,1.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,1.,0.,1.,1.,0.,0.,1.,1.,0.,1.,0.,0.,1.],
    [1.,1.,0.,0.,1.,1.,0.,0.,1.,0.,0.,1.,1.,0.,0.,0.,0.,1.,1.,0.,1.,0.,0.,1.,1.,0.,0.,1.,0.,1.,1.,0.],
    [1.,1.,0.,0.,0.,0.,1.,1.,1.,0.,0.,1.,0.,0.,1.,0.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,0.,1.,1.,0.],
    [0.,1.,1.,0.,0.,0.,1.,0.,0.,0.,1.,1.,0.,0.,1.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.],
    [0., 0., 1., 0., 0., 1., 1., 0., 0., 0., 1., 1., 1., 1., 0., 0., 0.,1., 1., 0., 0., 0., 1., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0.,0.,1.,0.,0.,1.,1.,0.,0.,0.,1.,1.,0.,0.,1.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.],
    [0., 1., 1., 1., 1., 0., 1., 0., 0., 0., 1., 1., 1., 1., 0., 0., 0.,
       0., 1., 1., 0., 1., 1., 0., 0., 0., 1., 1., 0., 0., 1., 1.],
    [0.    , 1.    , 0.    , 1.    , 0.    , 1.    , 1.    , 1.    ,
       1.    , 1.    , 0.    , 0.    , 0.0122, 0.0122, 1.    , 1.    ,
       0.    , 0.    , 1.    , 1.    , 0.    , 0.    , 1.    , 1.    ,
       0.    , 1.    , 1.    , 0.    , 1.    , 0.    , 0.    , 1.    ],
    [0.,0.,1.,0.,0.,1.,1.,0.,0.,0.,1.,1.,0.,0.,1.,1.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.],
    [1.,1.,0.,0.,1.,1.,0.,0.,1.,1.,0.,1.,0.,1.,0.,1.,0.,1.,1.,0.,1.,0.,0.,1.,1.,0.,1.,0.,0.,1.,0.,1.],
    [0., 0., 1., 0., 1., 0., 0., 1., 0., 0., 1., 1., 1., 1., 0., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 0., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 0., 0., 1., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 0., 1., 1., 0.],
    [0., 0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 1., 0.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 0., 1., 1., 0., 0., 1., 1., 0., 1., 0., 0., 1.],
    [1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0.,
        0., 1., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.],
    [0.    , 1.    , 0.    , 1.    , 0.    , 1.    , 1.    , 1.    , 1.    , 
     1.    , 0.    , 0.    , 0., 0., 1.    , 1.    , 0.    , 0.    , 1.    , 1.    , 
     0.    , 0.    , 1.    , 1.    , 0.    , 1.    , 1.    , 0.    , 1.    , 0.    , 0.    , 1.    ],
    [0., 0., 1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 0., 1.,
        1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 1., 0.]
]