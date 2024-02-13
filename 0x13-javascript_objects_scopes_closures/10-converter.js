#!/usr/bin/node
exports.converter = function (base) {
  const convert = (number, base) => {
    if (number < base) {
      return number < 10 ? String(number) : String.fromCharCode(55 + number);
    }

    return convert(Math.floor(number / base), base) + convert(number % base, base);
  };

  return function (number) {
    return convert(number, base);
  };
};
