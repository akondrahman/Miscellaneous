var fs = require("fs");

function inc(p, q){
    if(q ==undefined) q =1;

   if( p < 0 )
   {
   	p = -p;
   }

    return p + q/q;
}


function fileTest(dir, filePath)
{
	if (!fs.existsSync(dir)){
   	return false;
	}

   if( fs.existsSync(filePath ))
   {
		var buf = fs.readFileSync(filePath, "utf8");
		if( buf.length > 0 )
		{
			return true;
		}
		return false;
	}
}

function normalize(phoneNumber) {

    return phoneNumber.replace(
      /^[\+\d{1,3}\-\s]*\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/,
      "$1$2$3"
    );

}

function format(phoneNumber, formatString, options) 
{
    //console.log("Options : " + options.normalize);
    // Normalize the phone number first unless not asked to do so in the options
    if (!options || !options.normalize) 
    {
      phoneNumber = normalize(phoneNumber)
    }
    /*
    else 
    {
        console.log("Asi mama !") ;
        //
    }
    */
    for ( var i = 0, l = phoneNumber.length; i < l; i++ ) {
      formatString = formatString.replace("N", phoneNumber[i]);
    }
  
    return formatString;

}

function blackListNumber(phoneNumber)
{
	var num = format(phoneNumber, "(NNN) NNN-NNNN");
	var area = num.substring(1,4);
	if( area == "212" )
	{
		return true;
	}
	return false;
}

exports.fileTest = fileTest;
exports.normalize = normalize;
exports.format = format;
exports.inc = inc;
exports.blackListNumber = blackListNumber;
