/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const confirmed = emails.map((email)=>{
        let splited = email.split('@');
        return splited[0].split('+')[0].replace(/\./g, '') + '@' + splited[splited.length-1];
    });
    
    return [...new Set(confirmed)].length;
};
