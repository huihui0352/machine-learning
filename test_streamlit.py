import streamlit as st
from sklearn.metrics import accuracy_score
import pickle

st.title("***肾衰诊疗模型***")

##加载模型
with open('svm_model.pickle','rb') as file:
    svm_model=pickle.load(file)
    st.write("### svm model:\n",svm_model)

##加标签名称
with open ('label_name.pickle','rb') as file:
    label_names=pickle.load(file)
    st.write("### label names:\n",label_names)

##模型预测
##输入特征数据

s1=st.selectbox(label="便秘：",options=['yes','no'])
s2=st.selectbox(label="不欲饮食：",options=['yes','no'])
s3=st.selectbox(label="盗汗：",options=['yes','no'])
s4=st.selectbox(label="恶心：",options=['yes','no'])
s5=st.selectbox(label="浮肿：",options=['yes','no'])
s6=st.selectbox(label="口干：",options=['yes','no'])
s7=st.selectbox(label="口苦：",options=['yes','no'])
s9=st.selectbox(label="尿少：",options=['yes','no'])
s10=st.selectbox(label="神疲乏力：",options=['yes','no'])
s11=st.selectbox(label="头晕：",options=['yes','no'])
s12=st.selectbox(label="畏寒：",options=['yes','no'])
s13=st.selectbox(label="五心烦热：",options=['yes','no'])
s14=st.selectbox(label="腰酸：",options=['yes','no'])
s15=st.selectbox(label="舌淡白：",options=['yes','no'])
s16=st.selectbox(label="夜寐不安：",options=['yes','no'])
s17=st.selectbox(label="舌红：",options=['yes','no'])
s18=st.selectbox(label="舌胖大：",options=['yes','no'])
s19=st.selectbox(label="舌紫：",options=['yes','no'])
s20=st.selectbox(label="苔白：",options=['yes','no'])
s21=st.selectbox(label="苔黄：",options=['yes','no'])
s22=st.selectbox(label="苔腻：",options=['yes','no'])
s23=st.selectbox(label="脉数：",options=['yes','no'])
s24=st.selectbox(label="脉细：",options=['yes','no'])
s8=st.selectbox(label="脉弦：",options=['yes','no'])

with st.form(key="症状"):
    st.write("### 用户输入的特征数据：{}".format([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24]))
    submitted=st.form_submit_button("辨证")

if submitted:
    s1=0
    if s1=='yes':
        s1=1
    elif s1=='no':
        s1=0
    
    s2=0
    if s2=='yes':
        s2=1
    elif s2=='no':
        s2=0

    s3=0
    if s3=='yes':
        s3=1
    elif s3=='no':
        s3=0
    
    s4=0
    if s4=='yes':
        s4=1
    elif s4=='no':
        s5=0

    s5=0
    if s5=='yes':
        s5=1
    elif s5=='no':
        s5=0
   
    s6=0
    if s6=='yes':
        s6=1
    elif s6=='no':
        s6=0

    s7=0
    if s7=='yes':
        s7=1
    elif s7=='no':
        s7=0

    s8=0
    if s8=='yes':
        s8=1
    elif s8=='no':
        s8=0

    s9=0
    if s9=='yes':
        s9=1
    elif s9=='no':
        s9=0

    s10=0
    if s10=='yes':
        s10=1
    elif s10=='no':
        s10=0

    s11=0
    if s11=='yes':
        s11=1
    elif s11=='no':
        s11=0
    
    s12=0
    if s12=='yes':
        s12=1
    elif s12=='no':
        s12=0

    s13=0
    if s13=='yes':
        s13=1
    elif s13=='no':
        s13=0

    s14=0
    if s14=='yes':
        s14=1
    elif s14=='no':
        s14=0

    s15=0
    if s15=='yes':
        s15=1
    elif s15=='no':
        s15=0

    s16=0
    if s16=='yes':
        s16=1
    elif s16=='no':
        s16=0
    
    s17=0
    if s17=='yes':
        s17=1
    elif s17=='no':
        s17=0

    s18=0
    if s18=='yes':
        s18=1
    elif s18=='no':
        s18=0

    s19=0
    if s19=='yes':
        s19=1
    elif s19=='no':
        s19=0

    s20=0
    if s20=='yes':
        s20=1
    elif s20=='no':
        s20=0

    s21=0
    if s21=='yes':
        s21=1
    elif s21=='no':
        s21=0

    s22=0
    if s22=='yes':
        s22=1
    elif s22=='no':
        s22=0

    s23=0
    if s23=='yes':
        s23=1
    elif s23=='no':
        s23=0

    s24=0
    if s24=='yes':
        s24=1
    elif s24=='no':
        s24=0


    
     ##合并所有特征
    temp_feature=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24]
 
     ##模型预测
    new_prediction = svm_model.predict([temp_feature])

    #辨证选方
    predict_species=label_names[new_prediction][0]
    st.write("### 方：",predict_species)
