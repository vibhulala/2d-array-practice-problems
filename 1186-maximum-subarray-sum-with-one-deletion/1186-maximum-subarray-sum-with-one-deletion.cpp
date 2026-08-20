class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int nodeletion=arr[0];
        int onedeletion=INT_MIN;
        int result=arr[0];
        for (int i =1;i<arr.size();i++){
            int previousnodelete=nodeletion;
            int previousonedelete=onedeletion;
            nodeletion=max(nodeletion+arr[i],arr[i]);
            int b2;
            if (previousonedelete==INT_MIN){
                b2=arr[i];
            }
            else{
                b2=previousonedelete+arr[i];
            }
            onedeletion=max(b2,previousnodelete);
            result=max(result,max(onedeletion,nodeletion));
        }
        return result ;
    }
};