function solution(s) {
    const str = s
    const list_str = s.split(' ');
    
    const maxValue = Math.max.apply(null, list_str);
    const minValue = Math.min.apply(null, list_str);
      
    return String(minValue) + " " + String(maxValue)
  };



function solution(s) {
    const arr = s.split(' ');

    return Math.min(...arr)+' '+Math.max(...arr);
}
