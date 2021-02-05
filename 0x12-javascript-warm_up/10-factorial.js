#!/usr/bin/node
function fact (x)
{
  if (x === 1 || x == undefined)
  {
    return 1;
  }
  else
  {
    return (x * fact(x - 1));
  }
}
console.log(fact(process.argv[2]));
