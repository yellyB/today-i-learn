
var MyCalendarTwo = function() {
    this.calendar = [];
    this.overlaps = [];

    /**
    overlaps 에 예약이 겹치는 구간만 저장해둠.
    그러고서 예약 가능한지 체크할 때 overlaps를 먼저 확인함
    -> overlaps에 있으면 불가능한거고
    -> 없으면 캘린더 체크해서, 캘린더에 이미 있으면 overlaps에 겹치는 기간만큼 저장
     */
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendarTwo.prototype.book = function(start, end) {
    for(const [s, e] of this.overlaps){
        const startLimit = Math.max(s, start);
        const endLimit = Math.min(e, end);

        if(startLimit < endLimit) return false;
    }
    for(const [s, e] of this.calendar){
        const startLimit = Math.max(s, start);
        const endLimit = Math.min(e, end);

        if(startLimit < endLimit) this.overlaps.push([startLimit, endLimit]);
    }
    this.calendar.push([start, end]);

    return true;
};

/** 
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(start,end)
 */
