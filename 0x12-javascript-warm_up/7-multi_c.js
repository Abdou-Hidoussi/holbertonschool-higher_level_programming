#!/usr/bin/node
if (process.argv[2] == undefined)
{
    console.log('Missing number of occurrences');
}
else
{
    for (let x = 0; x < process.argv[2]; x++)
    {
        console.log('C is fun');
    }
}
