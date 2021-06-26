var c = artifacts.require("./healthSmartContract.sol");

module.exports = function(deployer) {
  deployer.deploy(c);
};
