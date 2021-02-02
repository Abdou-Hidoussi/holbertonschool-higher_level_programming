#!/usr/bin/node
len = process.argv.length;
if (len == 3)
{
    console.log("Argument found");
} 
else 
{
    if(len == 2)
    {
        console.log("No argument");
    }
    else
    {
        console.log("Arguments found");
    }
}