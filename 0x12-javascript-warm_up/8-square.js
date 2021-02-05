#!/usr/bin/node
if ((process.argv[2] == undefined) || (!parseInt(process.argv[2])))
{
  console.log('Missing size');
}
else
{
  for (let x = 0; x < process.argv[2]; x++)
  {
    console.log('X'.repeat(process.argv[2]));
  }
}
