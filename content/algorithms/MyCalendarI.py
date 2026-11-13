var MyCalendar = function() {
    this.calendar = [];
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function(start, end) {
    for(const [calendarStart, calendarEnd] of this.calendar){
        if(start < calendarEnd && calendarStart < end){
            return false;
        }
    }
    this.calendar.push([start, end])
    return true;
};

/** 
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
