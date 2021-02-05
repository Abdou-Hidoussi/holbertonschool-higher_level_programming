#!/usr/bin/node
const a = process.argv;
const b = parseInt(a)
if (process.argv.length <= 3)
{
  console.log(0);
}
else
{
  process.argv.sort(function(a, b)
  {
    return a - b;
  });
  console.log(process.argv);
}
