#!/usr/bin/node

exports.esrever = (list) => {
  const nList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    nList.push(list[i]);
  }
  return nList;
};
