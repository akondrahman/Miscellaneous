var subject = require('./subject.js')
var mock = require('mock-fs');
subject.inc(0, undefined);
subject.inc(-1, 0);
subject.blackListNumber('2120000000');
mock({"path/fileExists":{},"pathContent":{"file1":"text content","file2":""}});
	subject.fileTest('path/fileExists','pathContent/file2');
	subject.fileTest('path/fileExists','pathContent/file1');
mock.restore();
mock({});
	subject.fileTest('path/fileExists','pathContent/file1');
mock.restore();
mock({"path/fileExists":{}});
	subject.fileTest('path/fileExists','pathContent/file1');
mock.restore();
mock({"pathContent":{"file1":"text content","file2":""}});
	subject.fileTest('path/fileExists','pathContent/file1');
mock.restore();
subject.normalize('');
subject.format('','','');
subject.format('','',true);
var JSONObj = { "options ":"", "normalize":"true" };
subject.format('','',JSONObj);
subject.blackListNumber('');
