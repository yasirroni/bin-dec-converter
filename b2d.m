function y = b2d(x)
%% Original preface by Zacharias Voulgaris
% Convert a binary array to a decimal number
% Similar to bin2dec but works with arrays instead of strings and is found 
% to be rather faster
% Source: https://www.mathworks.com/matlabcentral/fileexchange/ ...
%   26447-efficient-convertors-between-binary-and-decimal-numbers

%% Preface
% Modification speed and array processing

%% Notes
% x in n,m matrix. n is the amount of binary and m is the length of the binary

%% Better Performance using polyval, suggestion by Matt D
y=zeros(size(x,1),1);
for i=1:size(x,1)
    y(i,1)=polyval(x(i,:),2);
end
