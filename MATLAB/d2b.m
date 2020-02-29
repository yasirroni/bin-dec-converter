function y = d2b(x,m)
%% Original preface by Zacharias Voulgaris
% Convert a decimanl number into a binary array
% Similar to dec2bin but yields a numerical array instead of a string and 
% is found to be rather faster
% Source: https://www.mathworks.com/matlabcentral/fileexchange/ ...
%   26447-efficient-convertors-between-binary-and-decimal-numbers

%% Preface
% Modification in error handling and array processing

%% Notes
% x can be columns or rows vector, must be in positive integer
% m length of output binary array

%% Biggest x
bigX=max(x);

%% Number of X to be converted
n=length(x);

%% Bug Fix from Marc Lalancette
c = max(0,floor(log2(bigX))) + 1;

%% Output Array
if nargin<2 % output array length is not defined by user
    m=c;
elseif m<c % output array is defined by user but smaller than required lenth
    m=c;
    disp('Determined Binnary Size Is Smaller Than Output Binnary Size')
end 

y = zeros(n,m); % Initialize output array 

%% Compute y
shift = m-c;
for i =1:n
    for j = 1:c
        r = floor(x(i) / 2);
        y(i,shift+c+1-j) = x(i) - 2*r;
        x(i) = r;
    end
end
