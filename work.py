#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sets = kümeler. İçinde farklı tipte veri barındırabilir.
#Boş bir set {} ve set() şeklinde oluşturulur.
#Kümelerde sıra yok. Her bastığında sıra değişebilir.
#Unique yapar. Tekrar etmez.
#Sıralama önemli değil.


# In[2]:


#Küme oluşturduk. LMS Playgrounda farklı bastı. Sıralama önemli değil.
set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
set_2 =set(colors)         .
print(set_1)
print(set_2)


# In[8]:


#Kerneli açıp kapattığımızda farklı sonuçlar alabiliriz. Elemaların sırası önemli değil.
letter = "a b c d e f g h i j k l m n o p r s t u v y z".split()
print(set(letter))                               


# In[9]:


#Boş küme yapmak için you can not use {}. The only way to create an empty set is set() function.
#İçi boş süslü parantez dictionary oluşturur.


# In[10]:


flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flowerset = set(flower_list)
flowerlist = list(flowerset)
print(flowerset) 
print(flowerlist)


# In[11]:


#Bunlar birbirinin aynısıdır. Çünkü küme elemanları unique.Çıktı aldığında eleman sayısı aynıdır.
print({'carnation', 'orchid', 'rose', 'violet'})
print({'rose', 'orchid', 'rose', 'violet', 'carnation'})


# In[13]:


#Çıktı aldığında eleman sayısı aynıdır.
a = {'carnation', 'orchid', 'rose', 'violet'}
b = {'rose', 'orchid', 'rose', 'violet', 'carnation'}
print(len(a))
print(len(b))


# In[14]:


#Main operations : .add() .remove() .intersection() .union() .difference() 


# In[20]:


#a kümesinin b kümesinden farkı 2 şekilde gösterilir:
a = set('philadelphia')
b = set('dolphin')
print(a - b)
print(a.difference(b))


# In[21]:


#b kümesinin a kümesinden farkı 2 şekilde yazılır:
a = set('philadelphia')
b = set('dolphin')
print(b - a)
print(b.difference(a))


# In[23]:


# a kümesi ile b kümesinin elemanlarının birleşimi
a = set('philadelphia')
b = set('dolphin')
print(a | b)
print(a.union(b))      
print(b | a)   # b kümesi ve a kümesinin elemanlarının birleşimi
print(b.union(a))


# In[25]:


#a ve b kümelerinin ortak elemanları:  
a = set('philadelphia')
b = set('dolphin')
print(a & b)
print(a.intersection(b))         
print(a & b == b & a)  #İkisi birbirine eşittir. 


# In[26]:


#Bazı işlemler & işareti boolean operations olan and yerine geçer.
#Bazı işlemler | işareti boolean operations olan or yerine geçer.


# In[27]:


current_date = set("07/04/2020") #Burada iterable olduğu için her birini ayrı ayrı eleman olarak küme yaptı.
current_date1 = {"07/04/2020"} #Bu satırda tek elemanlı bir küme yaptı.Çünkü tek bir elemanı paranteze aldık. O tek elamanlı bir kümeye dönüştü.
print(current_date)
print(current_date1)


# In[28]:


given_list = [1, 2 , 3, 3, 3, 3, 4, 4, 5, 5]
given_list = set([1, 2 , 3, 3, 3, 3, 4, 4, 5, 5])
given_list   # O listeyi aldık kümeye çevirdik.


# In[31]:


usa = set('Washington')
nz = set('Wellington')
print(usa)
print(nz)
print(usa.intersection(nz))
print(usa.union(nz))
print(usa.difference(nz))


# In[ ]:




