function [result]=AUC(test_targets,output)  
%计算AUC值,test_targets为原始样本标签,output为分类器得到的标签  
%均为行或列向量  
%test_targets = test_targets(1,1:5);
%output = output(:,1:5);
test_targets = test_targets(1,:);
[A,I]=sort(output(1,:),2);  
M=0;N=0;  
for i=1:length(output)  
    if(test_targets(i)==1)  
        M=M+1;  
    else  
        N=N+1;  
    end  
end  
sigma=0;  
for i=M+N:-1:1
    a = I(i);
    b = test_targets(I(i));
    if(test_targets(I(i))==1)  
        sigma=sigma+i;  
    end  
end  
result=(sigma-(M+1)*M/2)/(M*N); 