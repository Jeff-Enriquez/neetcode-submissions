class Logger {
public:
    queue<pair<int, string>> q;
    set<string> in_queue;
    Logger() {
        
    }
    
    bool shouldPrintMessage(int& timestamp, string& message) {
        while(!q.empty() && q.front().first <= timestamp - 10) {
            in_queue.erase(q.front().second);
            q.pop();
        }
        if(!in_queue.contains(message)) {
            in_queue.insert(message);
            q.push({timestamp, message});
            return true;
        }
        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
