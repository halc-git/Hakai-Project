#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,M;
    cin>>N>>M;
    vector<string> A(N);
    for(int i=0; i<N; i++){
        cin>>A[i];
    }
    vector<pair<int,vector<pair<int,int>>>> bomb(M);
    for(int i=0; i<M; i++){
        int C,L;
        bomb[i].first=C;
        for(int j=0; j<L; j++){
            int a,b;
            cin>>a>>b;
            bomb[i].second.push_back(make_pair(a,b));
        }
    }
    int x=-1,y=-1;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(A[i][j]=='@'){
                x=i;
                y=j;
                break;
            }
        }
        if(x!=-1)break;
    }
    vector<pair<int,string>> ans;
    for(int i=0; i<x; i++){
        ans.push_back(make_pair(1,"D"));
    }
    for(int i=0; i<y; i++){
        ans.push_back(make_pair(1,"R"));
    }
    for(int i=0; i<N*N; i++){
        ans.push_back(make_pair(2,to_string(1)));
    }
    for(int i=0; i<x; i++){
        ans.push_back(make_pair(1,"U"));
    }
    for(int i=0; i<y; i++){
        ans.push_back(make_pair(1,"L"));
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            ans.push_back(make_pair(3,to_string(1)));
            if(i==N-1&&j==N-1)break;
            else if(j==N-1)ans.push_back(make_pair(1,"D"));
            else if(i%2==0)ans.push_back(make_pair(1,"R"));
            else ans.push_back(make_pair(1,"L"));
        }
    }
    cout<<ans.size()<<endl;
    for(pair<int,string> i:ans){
        cout<<i.first<<" "<<i.second<<endl;
    }
}
