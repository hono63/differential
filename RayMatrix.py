
# coding: utf-8

# ## 光線行列
# - またはABCD行列
# 
#  \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  A & B \\
#  C & D
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}
#  
#  - 数式の書き方   
#   http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Typesetting%20Equations.html   
#   こことか https://kogler.wordpress.com/2008/03/21/latex-use-of-math-symbols-formulas-and-equations/

# In[24]:

import math
from Snell import snell


# ### 移行行列
#  \begin{align}
# y_2 = y_1 + d \tan \theta_1 \\
# \approx y_1 + d \theta_1 \\
# \theta_1 = \theta_2
#  \end{align}
#  
#   \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  1 & d \\
#  0 & 1
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}

# In[7]:

def move(y1, th1, d):
    y2 = y1 + d * math.tan(th1)
    th2 = th1
    return y2, th2


# ### 平面での屈折行列 
#  
#  \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  1 & 0 \\
#  0 & \frac{n_1}{n_2}
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}

# In[8]:

def refracPlain(y1, th1, n1, n2):
    y2 = y1
    th2 = th1 * n1 / n2
    return y2, th2


# ### 左凸レンズでの屈折
# 
#  \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  1 & 0 \\
#  -\frac{n_2-n_1}{Rn_2} & \frac{n_1}{n_2}
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}

# In[9]:

def refracLConvex(y1, th1, n1, n2, R):
    y2 = y1
    th2 = - y1 * (n2 - n1) / (R * n2) + th1 * n1 / n2
    return y2, th2


# In[32]:

# 左凸レンズの前側焦点距離
def focusLConvex(n1, n2, R):
    return R * n1 / (n2 - n1)


# ### 右凸レンズでの屈折
# 
# ここでRは負の値
# 
#  \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  1 & 0 \\
#  -\frac{n_2-n_1}{Rn_2} & \frac{n_1}{n_2}
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}

# In[51]:

def refracRConvex(y1, th1, n1, n2, R):
    y2 = y1
    th2 = y1 * (n2 - n1) / (R * n2) + th1 * n1 / n2
    return y2, th2


# In[53]:

# 右凸レンズの後ろ側焦点距離
def focusRConvex(n1, n2, R):
    return - R * n2 / (n2 - n1)


# ### 薄肉レンズでの屈折
# 
#  \begin{align}
#  \begin{pmatrix}
#  y_2 \\
#  \theta_2
#  \end{pmatrix} = 
#  \begin{pmatrix}
#  1 & 0 \\
#  -\frac{1}{f} & 1
#  \end{pmatrix}
#  \begin{pmatrix}
#  y_1 \\
#  \theta_1
#  \end{pmatrix}
#  \end{align}

# In[37]:

def refracConvex(y1, th1, focus):
    y2 = y1
    th2 = - y1 / focus + th1
    return y2, th2


# In[60]:

def refracConvex2(y1, th1, n1, n2, R):
    y2, th2 = refracLConvex(y1, th1, n1, n2, R)
    #print("y2:{0:.2f}, th2:{1:.2f}".format(y2, math.degrees(th2)))
    y3, th3 = refracRConvex(y2, th2, n2, n1, R)
    #print("y3:{0:.2f}, th3:{1:.2f}".format(y3, math.degrees(th3)))
    return y3, th3


# ### 焦点距離の合成
# 
#  \begin{align}
#  \frac{1}{f_1} + \frac{1}{f_2} = \frac{1}{f}
#  \end{align}

# In[58]:

def focusConvex(n1, n2, R):
    f1 = focusLConvex(n1, n2, R)    
    f2 = focusRConvex(n2, n1, R)
    finv = 1.0 / f1 + 1.0 / f2
    return 1.0 / finv


# In[59]:

# pyで保存。
import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'RayMatrix.ipynb'])


# In[ ]:



