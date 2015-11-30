var esprima = require("esprima");
var options = {tokens:true, tolerant: true, loc: true, range: true };
var faker = require("faker");
var fs = require("fs");
faker.locale = "en";
var mock = require('mock-fs');
var _ = require('underscore');
var Random = require('random-js');

var random = new Random();

function main()
{
	var args = process.argv.slice(2);

	if( args.length == 0 )
	{
		args = ["subject.js"];
	}
	var filePath = args[0];

	constraints(filePath);

	generateTestCases()

}


function fakeDemo()
{
	//console.log( faker.phone.phoneNumber() );
	//console.log( faker.phone.phoneNumberFormat() );
	//console.log( faker.phone.phoneFormats() );
}

var functionConstraints =
{
}

var mockFileLibrary = 
{
	pathExists:
	{
		'path/fileExists': {}
	},
	fileWithContent:
	{
		pathContent: 
		{	
  			file1: 'text content',
            file2: '',
		}
	}
};

var pAndQFlag  = false ;
var blackListPhoneFlag = false ; 

function generateTestCases()
{

	var content = "var subject = require('./subject.js')\nvar mock = require('mock-fs');\n";
	for ( var funcName in functionConstraints )
	{
		var params = {};

		// initialize params
		for (var i =0; i < functionConstraints[funcName].params.length; i++ )
		{
			var paramName = functionConstraints[funcName].params[i];
			//params[paramName] = '\'' + faker.phone.phoneNumber()+'\'';
			params[paramName] = '\'\'';
		}



		// update parameter values based on known constraints.
		var constraints = functionConstraints[funcName].constraints;
		// Handle global constraints...
		var fileWithContent = _.some(constraints, {mocking: 'fileWithContent' });
		var pathExists      = _.some(constraints, {mocking: 'fileExists' });
        
        


		for( var c = 0; c < constraints.length; c++ )
		{
			var constraint = constraints[c];
            
            //console.log("Constaint ! " + constraint.ident + "  value " + constraint.value );
			if( params.hasOwnProperty( constraint.ident ) )
			{
				params[constraint.ident] = constraint.value  || constraint.inverse ;
			}
		}

        if(funcName =="blackListNumber")
        {
            content += "subject.{0}({1});\n".format(funcName, constraint.inverse );
        }        
        //console.log( "Final params " +  params[0] + " " + params[1] );
        if(funcName =="inc")
        {
                content += "subject.{0}({1},{2});\n".format(funcName, constraint.value, constraint.inverse );
                //console.log('constraint of inc ' + constraint.inverse);
        }           
		// Prepare function arguments.
		var args = Object.keys(params).map( function(k) { return params[k]; }).join(",");
		if( pathExists || fileWithContent )
		{
			content += generateMockFsTestCases(pathExists,fileWithContent,funcName, args);
			// Bonus...generate constraint variations test cases....
			content += generateMockFsTestCases(!pathExists,!fileWithContent,funcName, args);
			content += generateMockFsTestCases(pathExists,!fileWithContent,funcName, args);
			content += generateMockFsTestCases(!pathExists,fileWithContent,funcName, args);
		}

		else
		{
			// Emit simple test case.
            content += "subject.{0}({1});\n".format(funcName, args );

		}

	}


	fs.writeFileSync('test.js', content, "utf8");

}

var bufFileLenFlag = true ;
var jsonObjFlag = true ;
function generateMockFsTestCases (pathExists,fileWithContent,funcName,args) 
{
	var testCase = "";
	// Insert mock data based on constraints.
	var mergedFS = {};
	if( pathExists )
	{
		for (var attrname in mockFileLibrary.pathExists) { mergedFS[attrname] = mockFileLibrary.pathExists[attrname]; }
	}
	if( fileWithContent )
	{
		for (var attrname in mockFileLibrary.fileWithContent) { mergedFS[attrname] = mockFileLibrary.fileWithContent[attrname]; }
	}
    


	testCase += 
	"mock(" +
		JSON.stringify(mergedFS)
		+
	");\n";
    
    /*To be automated do it in break today */
    if(bufFileLenFlag)
    {
        var buFileContent = "" ;
	    buFileContent =  "\tsubject.fileTest('path/fileExists','pathContent/file2');\n";
        testCase += buFileContent ;
        bufFileLenFlag = false; 
    }
    
    if(jsonObjFlag)
    {
        var jsonContent = "" ;
        jsonContent += "subject.format('','',true); \n";
        jsonContent += "var JSONObj = { 'options' :'', 'normalize':'true' }; \n";
        jsonContent += "subject.format('','',JSONObj); \n";    
        testCase +=    jsonContent ;
        jsonObjFlag = false ;
    }
    
	testCase += "\tsubject.{0}({1});\n".format(funcName, args );
	testCase+="mock.restore();\n";
    
    //console.log("test case ....");
    //console.log(testCase);    
    //console.log("....");    
	return testCase;
}

function constraints(filePath)
{
   var buf = fs.readFileSync(filePath, "utf8");
	var result = esprima.parse(buf, options);

	traverse(result, function (node) 
	{
		if (node.type === 'FunctionDeclaration') 
		{
			var funcName = functionName(node);
			//console.log("Line : {0} Function: {1}".format(node.loc.start.line, funcName ));

			var params = node.params.map(function(p) {return p.name});
            //console.log("Params :" + params );
			functionConstraints[funcName] = {constraints:[], params: params};

			// Check for expressions using argument.
			traverse(node, function(child)
			{
                
                /*
                
				if( child.type === 'BinaryExpression' && child.operator == ">")
				{
					if( child.left.type == 'Identifier' && params.indexOf( child.left.name ) > -1)
					{
						// get expression from original source code:
						//var expression = buf.substring(child.range[0], child.range[1]);
						var rightHand = buf.substring(child.right.range[0], child.right.range[1])
						functionConstraints[funcName].constraints.push( 
							{
								ident: child.left.name,
								value: rightHand
							});
					}
				}
                
                */
                
                //console.log("Rigth hand # 1 "+ rightHand );
                //var leftChildName = "" ;   
                //var rightHand ="";
                
                
                if( child.type === 'BinaryExpression' && child.operator == "<")
				{

                    var leftChildName = child.left.name ;
					if( child.left.type == 'Identifier' && params.indexOf( leftChildName ) > -1)
					{
						// get expression from original source code:
						//var expression = buf.substring(child.range[0], child.range[1]);
						var rightHand = buf.substring(child.right.range[0], child.right.range[1]);
                        //var rightHand = -1 ;
						functionConstraints[funcName].constraints.push( 
							{
								ident: child.left.name,
                                value: random.integer( rightHand - 10, rightHand -1 ), 
                                inverse: random.integer( rightHand, rightHand )
							});
                        


                        
					}
				}
                
                //console.log("Left hand for <  "+ leftChildName  + " value " + rightHand ) ;
                
				if( child.type === 'BinaryExpression' && child.operator == "==")
				{
					if( child.left.type == 'Identifier' && params.indexOf( child.left.name ) > -1)
					{
						// get expression from original source code:
						//var expression = buf.substring(child.range[0], child.range[1]);
						var rightHand = buf.substring(child.right.range[0], child.right.range[1]);
						functionConstraints[funcName].constraints.push( 
							{
								ident: child.left.name,
								value: rightHand
							});
                        
                        /*
                        
						var rightHandX = buf.substring(child.right.range[0], child.right.range[1]);
                        rightHandX = 0 ;
						functionConstraints[funcName].constraints.push( 
							{
								ident: child.left.name,
								value: rightHandX
							});                        
                        */
					}
				}
                
                //console.log("Rigth hand # 3 "+ rightHand );

				if( child.type == "CallExpression" && 
					 child.callee.property &&
					 child.callee.property.name =="readFileSync" )
				{
					for( var p =0; p < params.length; p++ )
					{
						if( child.arguments[0].name == params[p] )
						{
							functionConstraints[funcName].constraints.push( 
							{
								// A fake path to a file
								ident: params[p],
								value: "'pathContent/file1'",
								mocking: 'fileWithContent'
							});
						}
					}
				}

				if( child.type == "CallExpression" &&
					 child.callee.property &&
					 child.callee.property.name =="existsSync")
				{
					for( var p =0; p < params.length; p++ )
					{
						if( child.arguments[0].name == params[p] )
						{
							functionConstraints[funcName].constraints.push( 
							{
								// A fake path to a file
								ident: params[p],
								value: "'path/fileExists'",
								mocking: 'fileExists'
							});
						}
					}
				}

                if( child.type == "CallExpression" &&
					 child.callee.property &&
					 funcName =="blackListNumber")
				{

                    var tempRand =  "'" + random.integer(  1000000000, 9999999999 ) + "'" ;
                    //console.log('temp ' + tempRand);
					for( var p =0; p < params.length; p++ )
					{
                        //console.log('black list e asi mama ');                            
						functionConstraints[funcName].constraints.push( 
						{
                                
								ident: params[p],
                                //value: random.integer( rightHand - 10, rightHand -1 ), 
                                value: "'2120000000'", 
                                inverse:  tempRand
						});
						
					}
				}                
                
                 

			});

			//console.log( functionConstraints[funcName]);

		}
	});
}

function traverse(object, visitor) 
{
    var key, child;

    visitor.call(null, object);
    for (key in object) {
        if (object.hasOwnProperty(key)) {
            child = object[key];
            if (typeof child === 'object' && child !== null) {
                traverse(child, visitor);
            }
        }
    }
}

function traverseWithCancel(object, visitor)
{
    var key, child;

    if( visitor.call(null, object) )
    {
	    for (key in object) {
	        if (object.hasOwnProperty(key)) {
	            child = object[key];
	            if (typeof child === 'object' && child !== null) {
	                traverseWithCancel(child, visitor);
	            }
	        }
	    }
 	 }
}

function functionName( node )
{
	if( node.id )
	{
		return node.id.name;
	}
	return "";
}


if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

main();