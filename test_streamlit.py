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
s3=st.selectbox(label="大便溏薄：",options=['yes','no'])
s4=st.selectbox(label="盗汗：",options=['yes','no'])
s5=st.selectbox(label="恶心：",options=['yes','no'])
s6=st.selectbox(label="浮肿：",options=['yes','no'])
s7=st.selectbox(label="腹胀：",options=['yes','no'])
s8=st.selectbox(label="口干：",options=['yes','no'])
s9=st.selectbox(label="口苦：",options=['yes','no'])
s10=st.selectbox(label="面色白：",options=['yes','no'])
s11=st.selectbox(label="面色萎黄：",options=['yes','no'])
s12=st.selectbox(label="尿少：",options=['yes','no'])
s13=st.selectbox(label="尿中带泡沫：",options=['yes','no'])
s14=st.selectbox(label="气短：",options=['yes','no'])
s15=st.selectbox(label="神疲乏力：",options=['yes','no'])
s16=st.selectbox(label="头晕：",options=['yes','no'])
s17=st.selectbox(label="畏寒：",options=['yes','no'])
s18=st.selectbox(label="五心烦热：",options=['yes','no'])
s19=st.selectbox(label="腰酸：",options=['yes','no'])
s20=st.selectbox(label="腰痛：",options=['yes','no'])
s21=st.selectbox(label="夜寐不安：",options=['yes','no'])
s22=st.selectbox(label="舌淡白：",options=['yes','no'])
s23=st.selectbox(label="舌光：",options=['yes','no'])
s24=st.selectbox(label="舌红：",options=['yes','no'])
s25=st.selectbox(label="舌胖大：",options=['yes','no'])
s26=st.selectbox(label="舌紫：",options=['yes','no'])
s27=st.selectbox(label="苔白：",options=['yes','no'])
s28=st.selectbox(label="苔黄：",options=['yes','no'])
s29=st.selectbox(label="苔腻：",options=['yes','no'])
s30=st.selectbox(label="脉滑：",options=['yes','no'])
s31=st.selectbox(label="脉数：",options=['yes','no'])
s32=st.selectbox(label="脉细：",options=['yes','no'])

with st.form(key="症状"):
    submitted=st.form_submit_button("辨证选方")

if submitted:
    s1=0
    if s1=='有':
        s1=1
    elif s1=='无':
        s1=0
    
    s2=0
    if s2=='有':
        s2=1
    elif s2=='无':
        s2=0

    s3=0
    if s3=='有':
        s3=1
    elif s3=='无':
        s3=0
    
    s4=0
    if s4=='有':
        s4=1
    elif s4=='无':
        s5=0

    s5=0
    if s5=='有':
        s5=1
    elif s5=='无':
        s5=0
   
    s6=0
    if s6=='有':
        s6=1
    elif s6=='无':
        s6=0

    s7=0
    if s7=='有':
        s7=1
    elif s7=='无':
        s7=0

    s8=0
    if s8=='有':
        s8=1
    elif s8=='无':
        s8=0

    s9=0
    if s9=='有':
        s9=1
    elif s9=='无':
        s9=0

    s10=0
    if s10=='有':
        s10=1
    elif s10=='无':
        s10=0

    s11=0
    if s11=='有':
        s11=1
    elif s11=='无':
        s11=0
    
    s12=0
    if s12=='有':
        s12=1
    elif s12=='无':
        s12=0

    s13=0
    if s13=='有':
        s13=1
    elif s13=='无':
        s13=0

    s14=0
    if s14=='有':
        s14=1
    elif s14=='无':
        s14=0

    s15=0
    if s15=='有':
        s15=1
    elif s15=='无':
        s15=0

    s16=0
    if s16=='有':
        s16=1
    elif s16=='无':
        s16=0
    
    s17=0
    if s17=='有':
        s17=1
    elif s17=='无':
        s17=0

    s18=0
    if s18=='有':
        s18=1
    elif s18=='无':
        s18=0

    s19=0
    if s19=='有':
        s19=1
    elif s19=='无':
        s19=0

    s20=0
    if s20=='有':
        s20=1
    elif s20=='无':
        s20=0

    s21=0
    if s21=='有':
        s21=1
    elif s21=='无':
        s21=0

    s22=0
    if s22=='有':
        s22=1
    elif s22=='无':
        s22=0

    s23=0
    if s23=='有':
        s23=1
    elif s23=='无':
        s23=0

    s24=0
    if s24=='有':
        s24=1
    elif s24=='无':
        s24=0
    
    s25=0
    if s25=='有':
        s25=1
    elif s25=='无':
        s25=0
    
    s26=0
    if s26=='有':
        s26=1
    elif s26=='无':
        s26=0

    s27=0
    if s27=='有':
        s27=1
    elif s27=='无':
        s27=0

    s28=0
    if s28=='有':
        s28=1
    elif s28=='无':
        s28=0

    s29=0
    if s29=='有':
        s29=1
    elif s29=='无':
        s29=0

    s30=0
    if s30=='有':
        s30=1
    elif s30=='无':
        s30=0

    s31=0
    if s31=='有':
        s31=1
    elif s31=='无':
        s31=0

    s32=0
    if s32=='有':
        s32=1
    elif s32=='无':
        s32=0


    
     ##合并所有特征
    temp_feature=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32]
 
     ##模型预测
    new_prediction = svm_model.predict([temp_feature])

    #辨证选方
    predict_species=label_names[new_prediction][0]
    st.write("### 方：",predict_species)

