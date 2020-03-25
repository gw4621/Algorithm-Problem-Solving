#define ALEN 26

struct Trie{
    bool end;
	int next[ALEN];
    int count;
} node[1000001];
int nextIdx;

void init(void) {
    node[0].end = false;
    node[0].count = 0;
    for(int i=0;i<ALEN;i++){
    	node[0].next[i] = -1;
    }
    nextIdx = 1;
}

void insert(int buffer_size, char *buf) {
    int n = 0, b = 0, ch;
    while(b < buffer_size){
        ch = buf[b] - 97;
        if(node[n].next[ch] < 0){
        	node[n].next[ch] = nextIdx;
            node[nextIdx].end = false;
            node[nextIdx].count = 0;
            for(int i=0;i<ALEN;i++){
            	node[nextIdx].next[i] = -1;
            }
            nextIdx += 1;
        }
        n = node[n].next[ch];
        node[n].count += 1;
        b += 1;
    }
    node[n].end = true;
}

int query(int buffer_size, char *buf) {
    int i, ch, n = 0;
    for(i=0;i<buffer_size;i++){
        ch = buf[i]-97;
    	if(node[n].next[ch] < 0) return 0;
        n = node[n].next[ch];        
    }
    return node[n].count;
}