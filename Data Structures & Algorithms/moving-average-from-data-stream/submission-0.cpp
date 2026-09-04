class MovingAverage {
public:
    deque<int> q;
    int max_size;
    int curr_size = 0;
    double sum = 0;
    MovingAverage(int size) {
        max_size = size;
    }
    
    double next(int val) {
        q.push_front(val);
        sum += val;
        if(q.size() > max_size) {
            sum -= q.back();
            q.pop_back();
        }
        return sum / q.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
