let athleteFinalPosition = 'first place';
switch (athleteFinalPosition) {
  case 'first place':
  console.log('You get the gold medal!');
  break;
  case 'second place':
  console.log('You get the silver medal!');
  break;
  case 'third place':
  console.log('You get the bronze medal!');
  break;
  default:
  console.log('No medal awarded.');
  break;

    
    // In this activity I learned about the switch statement and how it provides an easier syntax compared to if...else statements.
    // I learned that the "switch" keyword  initiates the statement and the value of the statement is followed with parentheses.
    // Then inside the code block {} there are multiple case(s) that checks if the expression matches the specified value that comes after it.
    // If the value of the switch statement matches the declared variable then the console.log() associated will run or any related statement.
    // Else the default statement will run.
    // Note: the keyword "break" tells the computer to exit the block and not execute any more code or check any other cases inside the code block.
    // Without "break" the first matching case will run, but so will every subsequent case regardless of whether or not it matches.
