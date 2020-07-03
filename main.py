#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.head()


# In[4]:


black_friday.info()


# In[5]:


black_friday.isna().sum()


# In[17]:


black_friday.dtypes.value_counts()


# In[23]:


black_friday['Age'].value_counts()


# In[24]:


pd.crosstab(black_friday.Gender,black_friday.Age)


# In[66]:


#nulos em Product_Category_2
len(black_friday.query("Product_Category_2 == 'NaN'"))


# In[67]:


#nulos em Product_Category_3
len(black_friday.query("Product_Category_3 == 'NaN'"))


# In[69]:


# Quantidade de valores nulos em Product_Category_2 que NÃO são nulos em Product_Category_3
len(black_friday.query("Product_Category_2 == 'NaN' & Product_Category_3 != 'NaN'"))


# In[70]:


# Quantidade de valores nulos em Product_Category_2 que TAMBÉM são nulos em Product_Category_3
len(black_friday.query("Product_Category_2 == 'NaN' & Product_Category_3 == 'NaN'"))


# In[94]:


def q10():
    # Retorne aqui o resultado da questão 10.
   return bool(len(black_friday.query("Product_Category_2=='NaN' & Product_Category_3=='NaN'")))
 
q10()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[22]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape 
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[26]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return black_friday.query("Gender == 'F' & Age == '26-35'").shape[0]
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[28]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday.User_ID.nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[35]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return (black_friday.shape[0]-black_friday.dropna().shape[0])/black_friday.shape[0]
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[39]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday.isna().sum().max()
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[48]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return float(black_friday.Product_Category_3.mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[87]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return ((black_friday['Purchase'] - black_friday['Purchase'].min())/
           (black_friday['Purchase'].max()-black_friday['Purchase'].min())).mean()
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[99]:


def q9():
    # Retorne aqui o resultado da questão 9.
    purchase_stand = (black_friday.Purchase - black_friday.Purchase.mean()) / black_friday.Purchase.std()
    return len(purchase_stand[(purchase_stand > -1) & (purchase_stand < 1)])
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[100]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return bool(len(black_friday.query("Product_Category_2=='NaN' & Product_Category_3=='NaN'")))
    pass


# In[ ]:




