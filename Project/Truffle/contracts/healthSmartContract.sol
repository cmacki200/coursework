pragma solidity ^0.5.16;

contract healthSmartContract {

  struct Patient{

   string name;
   int age;
   string gender;
 }

 Patient private patient;
 address public recordOwner;

  modifier onlyOwner() {
  require(msg.sender == recordOwner);
  _;
}


function patientRecord() public{
  recordOwner = msg.sender;
}

function getPatient() public view returns (string memory name, int age,
  string memory gender){
  return (patient.name, patient.age, patient.gender);
  }

  function setPatient (string memory _name, int _age, string memory  _gender) public{
      patient.name = _name;
      patient.age = _age;
      patient.gender = _gender;
  }

}
