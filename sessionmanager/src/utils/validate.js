const parseError = error => {
  /*
    Parse Errors from Backend
    */
  let reg = new RegExp('\\[(.*?)]');
  let match = String(reg.exec(error)[1]);
  console.log(match);
  return match;
};

/*
    Exceptions for backend operations
*/
const exceptions = [
  {
    code: 'NoRawFiles',
    helpText: 'There are no .CR2 files in this path.'
  },
  {
    code: 'SessionExists',
    helpText: 'This Session already exists.'
  },
  {
    code: 'Error',
    helpText: 'Some Error'
  }
];

export const Exception = (error, parse = false) => {
  let code;
  if (parse) {
    code = parseError(error);
  } else {
    code = error;
  }
  let exc = exceptions.filter(e => e.code == code)[0];
  return exc;
};
