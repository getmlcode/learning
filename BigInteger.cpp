#include<iostream.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
#define SIZE 10000

//================================Class For Handling Large Integers==================================\\

class BigInteger
{
    private:

        // state variables
        char CharInt[SIZE],sign;
        unsigned int No_Of_Digits;
        unsigned int First_NonZero_Digit_Index;

        void Align()                        // To Right Justify The Numbers
            {
                int i;
                char k;

                k = CharInt[0];             // To Detect Leading Zeros In Input

                if(sign == '+')
                {
                    for( i =0; i<No_Of_Digits; i++ )
                        {
                            CharInt[SIZE-1-i] = CharInt[No_Of_Digits-i-1];
                        }
                }

                else if(sign == '-')
                {
                    for( i =0; i<No_Of_Digits; i++ )
                        {
                            CharInt[SIZE-1-i] = CharInt[No_Of_Digits-i];
                        }
                }

                for(i=0; i< SIZE-No_Of_Digits; i++)
                {
                    CharInt[i] = '0';
                }

                if( k == '0')
                {
                    Adjust();
                }

            }

        void Adjust()                       // To Maintain The Consistent State Of The Object
            {
                int i;

                for( i=0; i<SIZE; i++ )
                    {
                        if( CharInt[i] == '0')
                            {
                                continue;
                            }
                        else
                            {
                                break;
                            }
                    }

                if( i < SIZE )
                    {
                        No_Of_Digits = SIZE-i;
                        First_NonZero_Digit_Index = SIZE - No_Of_Digits;
                    }
                else if( i == SIZE )
                    {
                        No_Of_Digits = 1;
                        First_NonZero_Digit_Index = SIZE - 1;
                    }
            }

    public :

        BigInteger()
            {
                int i;
                for( i=0; i<SIZE; i++)
                    {

                        CharInt[i]='0';
                    }

                No_Of_Digits = 1;
                First_NonZero_Digit_Index = SIZE - 1;
            }

        BigInteger( char INT[] )
            {
                short k = 0;

                strcpy(CharInt,INT);

                if( CharInt[0] == '-')
                    {
                        k=1;
                    }

                for(int i =k; i<strlen(CharInt); i++)
                    {
                        if(CharInt[i] > 57 || CharInt[i] < 48)
                            {
                                cout<<"\nWrong Initialization!! \nBigInteger Object Takes Only Numeric Values\n";
                                exit(0);
                            }
                    }

                if(CharInt[0] == '-')
                {
                    No_Of_Digits = strlen(CharInt)-1;
                    sign = '-';
                }
                else
                {
                    No_Of_Digits = strlen(CharInt);
                    sign = '+';
                }

                First_NonZero_Digit_Index = SIZE - No_Of_Digits;
                Align();
            }

        void operator=( char INT[] )        // Assignment fucntion
            {
                short k=0;

                strcpy(CharInt,INT);

                if( CharInt[0] == '-')
                    {
                        k=1;
                    }

                for(int i =k; i<strlen(CharInt); i++)
                    {
                        if(CharInt[i] > 57 || CharInt[i] < 48)
                            {
                                cout<<"\nAttempting To Assign Non Numeric Value To BigInteger Object!!\n";
                                cout<<"BigInteger Object Takes Only Numeric Values\n";
                                exit(0);
                            }
                    }

                if(CharInt[0] == '-')
                {
                    No_Of_Digits = strlen(CharInt)-1;
                    sign = '-';
                }
                else
                {
                    No_Of_Digits = strlen(CharInt);
                    sign = '+';
                }

                First_NonZero_Digit_Index = SIZE - No_Of_Digits;
                Align();
            }

        void NumberOfDigits();                                                      //Display The Number Of Digits In The Number
        void TrailingZeroDisplay();                                                 //Display The Number With Trailing Zeros
        void ShiftLeft( int No_Of_Shifts );                                         //Left Shift The Number By Given Amount
        void ShiftRight( int No_Of_Shifts );                                        //Left Shift The Number By Given Amount

        //---------------------------Input/Output Stream Connectivity Functions------------------------\\

        friend istream& operator>>( istream& Input, BigInteger& Number );

        friend ostream& operator<<( ostream& Output, BigInteger& Number );


        //------------------------Functions For Comparing With Non Objects-----------------------------\\

        short operator==( char Number[] )
            {
                BigInteger Temp;
                short Equal=1;

                Temp = Number;

                if( *this == Temp )
                    {
                        return Equal;
                    }
                else
                    {
                        Equal = 0;
                        return Equal;
                    }
            }

        short operator!=( char Number[] )
            {
                BigInteger Temp;
                short NotEqual=1;

                Temp = Number;

                if( *this != Temp )
                    {
                        return NotEqual;
                    }
                else
                    {
                        NotEqual = 0;
                        return NotEqual;
                    }
            }

        short operator>( char Number[] )
            {
                BigInteger Temp;
                short Greater=1;

                if( *this > Temp )
                    {
                        return Greater;
                    }
                else
                    {
                        Greater = 0;
                        return Greater;

                    }
            }
        short operator>=( char Number[] )
            {
                BigInteger Temp;
                short Greater=1;

                Temp = Number;

                if( *this >= Temp )
                    {
                        return Greater;
                    }
                else
                    {
                        Greater = 0;
                        return Greater;
                    }
            }

        short operator<( char Number[] )
            {
                BigInteger Temp;
                short Smaller=1;

                Temp = Number;

                if( *this < Temp )
                    {
                        return Smaller;
                    }
                else
                    {
                        Smaller = 0;
                        return Smaller;
                    }
            }

        short operator<=( char Number[] )
            {
                BigInteger Temp;
                short Smaller=1;

                Temp = Number;

                if( *this <=Temp )
                    {
                        return Smaller;
                    }
                else
                    {
                        Smaller = 0;
                        return Smaller;
                    }
            }

        //-----------------------------Functions For Comparing Between Objects-------------------------\\

        short operator!=( BigInteger& SecondNumber )
            {
                short NotEqual = 1;
                int i;

                if( *this == SecondNumber )
                    {
                        NotEqual = 0 ;
                        return NotEqual;
                    }
                else
                    {
                        return NotEqual;
                    }
            }

        short operator==( BigInteger& SecondNumber )
            {
                short Equal = 1;
                int i;
                if( sign == SecondNumber.sign )
                {
                    if( No_Of_Digits > SecondNumber.No_Of_Digits )
                        {
                            Equal=0;
                            return Equal;
                        }
                    else if( No_Of_Digits < SecondNumber.No_Of_Digits )
                        {
                            Equal=0;
                            return Equal;
                        }
                    else
                        {
                            for( i=First_NonZero_Digit_Index; i<SIZE; i++)
                                {
                                    if( CharInt[i] == SecondNumber.CharInt[i])
                                        {
                                            continue;
                                        }
                                    else if( CharInt[i] > SecondNumber.CharInt[i])
                                        {
                                            Equal=0;
                                            break;
                                        }
                                    else if( CharInt[i] < SecondNumber.CharInt[i])
                                        {
                                            Equal=0;
                                            break;
                                        }
                                }
                        }
                }
                else
                {
                    Equal = 0;
                }

                return Equal;
            }

        short operator>( BigInteger& SecondNumber )
            {
                short Greater = 1;
                int i=0;

                if( sign == '-' && SecondNumber.sign == '+' )
                {
                    Greater = 0;
                    return Greater;
                }

                else if( sign == SecondNumber.sign )
                {
                    if( No_Of_Digits > SecondNumber.No_Of_Digits  )
                        {
                            if( sign == '+')
                                {
                                    return Greater;
                                }
                            else
                                {
                                    Greater = 0;
                                    return Greater;
                                }
                        }
                    else if( No_Of_Digits < SecondNumber.No_Of_Digits )
                        {
                            if( sign == '+')
                                {
                                    Greater=0;
                                    return Greater;
                                }
                            else
                                {
                                    return Greater;
                                }
                        }
                    else
                        {
                            for( i=First_NonZero_Digit_Index; i<SIZE; i++)
                                {
                                    if( CharInt[i] == SecondNumber.CharInt[i])
                                        {
                                            continue;
                                        }
                                    else if( CharInt[i] > SecondNumber.CharInt[i])
                                        {
                                            if( sign == '+')
                                                {
                                                    return Greater;
                                                }
                                            else
                                                {
                                                    Greater = 0;
                                                    return Greater;
                                                }

                                        }
                                    else if( CharInt[i] < SecondNumber.CharInt[i])
                                        {
                                            if( sign == '+')
                                                {
                                                    Greater=0;
                                                    return Greater;
                                                }
                                            else
                                                {
                                                    return Greater;
                                                }
                                        }
                                }
                        }
                }


                if(i==SIZE)
                    {
                        Greater=0;
                        return Greater;
                    }
                else
                    {
                        return Greater;
                    }

            }

        short operator>=( BigInteger& SecondNumber )
            {
                short Greater = 1;
                int i=0;

                if( sign == '-' && SecondNumber.sign == '+' )
                {
                    Greater = 0;
                    return Greater;
                }

                else if( sign == SecondNumber.sign )
                {
                    if( No_Of_Digits > SecondNumber.No_Of_Digits  )
                        {
                            if( sign == '+')
                                {
                                    return Greater;
                                }
                            else
                                {
                                    Greater = 0;
                                    return Greater;
                                }
                        }
                    else if( No_Of_Digits < SecondNumber.No_Of_Digits )
                        {
                            if( sign == '+')
                                {
                                    Greater=0;
                                    return Greater;
                                }
                            else
                                {
                                    return Greater;
                                }
                        }
                    else
                        {
                            for( i=First_NonZero_Digit_Index; i<SIZE; i++)
                                {
                                    if( CharInt[i] == SecondNumber.CharInt[i])
                                        {
                                            continue;
                                        }
                                    else if( CharInt[i] > SecondNumber.CharInt[i])
                                        {
                                            if( sign == '+')
                                                {
                                                    return Greater;
                                                }
                                            else
                                                {
                                                    Greater = 0;
                                                    return Greater;
                                                }

                                        }
                                    else if( CharInt[i] < SecondNumber.CharInt[i])
                                        {
                                            if( sign == '+')
                                                {
                                                    Greater=0;
                                                    return Greater;
                                                }
                                            else
                                                {
                                                    return Greater;
                                                }
                                        }
                                }
                        }
                }

                return Greater;
            }

        short operator<( BigInteger& SecondNumber )
            {
                short Smaller = 1;
                int i=0;

                if( sign == '+' && SecondNumber.sign == '-' )
                {
                    Smaller = 0;
                    return Smaller;
                }

                else if( sign == SecondNumber.sign )
                {
                    if( No_Of_Digits > SecondNumber.No_Of_Digits  )
                        {
                            if( sign == '-')
                                {
                                    return Smaller;
                                }
                            else
                                {
                                    Smaller = 0;
                                    return Smaller;
                                }
                        }
                    else if( No_Of_Digits < SecondNumber.No_Of_Digits )
                        {
                            if( sign == '-')
                                {
                                    Smaller=0;
                                    return Smaller;
                                }
                            else
                                {
                                    return Smaller;
                                }
                        }
                    else
                        {
                            for( i=First_NonZero_Digit_Index; i<SIZE; i++)
                                {
                                    if( CharInt[i] == SecondNumber.CharInt[i])
                                        {
                                            continue;
                                        }
                                    else if( CharInt[i] > SecondNumber.CharInt[i])
                                        {
                                            if( sign == '-')
                                                {
                                                    return Smaller;
                                                }
                                            else
                                                {
                                                    Smaller = 0;
                                                    return Smaller;
                                                }

                                        }
                                    else if( CharInt[i] < SecondNumber.CharInt[i])
                                        {
                                            if( sign == '-')
                                                {
                                                    Smaller=0;
                                                    return Smaller;
                                                }
                                            else
                                                {
                                                    return Smaller;
                                                }
                                        }
                                }
                        }
                }


                if(i==SIZE)
                    {
                        Smaller=0;
                        return Smaller;
                    }
                else
                    {
                        return Smaller;
                    }

            }

        short operator<=( BigInteger& SecondNumber )
            {
                short Smaller = 1;
                int i=0;

                if( sign == '+' && SecondNumber.sign == '-' )
                {
                    Smaller = 0;
                    return Smaller;
                }

                else if( sign == SecondNumber.sign )
                {
                    if( No_Of_Digits > SecondNumber.No_Of_Digits  )
                        {
                            if( sign == '-')
                                {
                                    return Smaller;
                                }
                            else
                                {
                                    Smaller = 0;
                                    return Smaller;
                                }
                        }
                    else if( No_Of_Digits < SecondNumber.No_Of_Digits )
                        {
                            if( sign == '-')
                                {
                                    Smaller=0;
                                    return Smaller;
                                }
                            else
                                {
                                    return Smaller;
                                }
                        }
                    else
                        {
                            for( i=First_NonZero_Digit_Index; i<SIZE; i++)
                                {
                                    if( CharInt[i] == SecondNumber.CharInt[i])
                                        {
                                            continue;
                                        }
                                    else if( CharInt[i] > SecondNumber.CharInt[i])
                                        {
                                            if( sign == '-')
                                                {
                                                    return Smaller;
                                                }
                                            else
                                                {
                                                    Smaller = 0;
                                                    return Smaller;
                                                }

                                        }
                                    else if( CharInt[i] < SecondNumber.CharInt[i])
                                        {
                                            if( sign == '-')
                                                {
                                                    Smaller=0;
                                                    return Smaller;
                                                }
                                            else
                                                {
                                                    return Smaller;
                                                }
                                        }
                                }
                        }
                }

                return Smaller;

            }

        //-----------------------------Functions For Comparing Between Objects Ends----------------------------\\


        //--------------------------------------Basic Arithmetic Fucntions-------------------------------------\\

        BigInteger operator+(BigInteger& Integer)                                   /*Adding The Large Numbers*/
            {
                BigInteger IntermediateResult,LeftOp,RightOp;
                char First_Op_Digit,Second_Op_Digit,Result_Digit;
                short carry = 0;
                int i;

                LeftOp = *this;
                RightOp = Integer;

                if(LeftOp.sign == '+' && RightOp.sign == '+')
                {
                    for( i=SIZE-1; i>=0; i-- )
                        {
                            First_Op_Digit = LeftOp.CharInt[i]-48;
                            Second_Op_Digit = RightOp.CharInt[i]-48;

                            Result_Digit =  ( First_Op_Digit + Second_Op_Digit + carry )%10;
                            carry = ( First_Op_Digit + Second_Op_Digit + carry )/10;
                            IntermediateResult.CharInt[i] = Result_Digit + 48;
                        }
                IntermediateResult.Adjust();
                IntermediateResult.sign = '+';
                }

                else if(sign == '-' && Integer.sign == '-')
                {
                    for( i=SIZE-1; i>=0; i-- )
                        {
                            First_Op_Digit = LeftOp.CharInt[i]-48;
                            Second_Op_Digit = RightOp.CharInt[i]-48;

                            Result_Digit =  ( First_Op_Digit + Second_Op_Digit + carry )%10;
                            carry = ( First_Op_Digit + Second_Op_Digit + carry )/10;
                            IntermediateResult.CharInt[i] = Result_Digit + 48;
                        }
                IntermediateResult.Adjust();
                IntermediateResult.sign = '-';
                }

                else if(sign == '+' && Integer.sign == '-')
                {
                    RightOp.sign = '+';
                    IntermediateResult = LeftOp-RightOp;
                }

                else if(sign == '-' && Integer.sign == '+')
                {
                    LeftOp.sign = '+';
                    IntermediateResult = RightOp-LeftOp;
                }

                if(carry != 0)
                    {
                        cout<<"\nOverflow Occured!!!!";
                        exit(0);
                    }

                return IntermediateResult;
            }

        BigInteger operator-(BigInteger& Integer)   //Subtracting The Large Numbers
            {
                BigInteger IntermediateResult,One("1"),LeftOp,RightOp;
                char First_Op_Digit,Second_Op_Digit,Result_Digit;
                short flag=-1;
                int i,No_Of_TensComplement_Digits;

                LeftOp = *this;
                RightOp = Integer;

                if( LeftOp == "0" && RightOp.sign == '+' )
                    {
                        RightOp.sign = '-';
                        return RightOp;
                    }

                else if( LeftOp == "0" && RightOp.sign == '-' )
                    {
                        RightOp.sign = '+';
                        return RightOp;
                    }

                else if( LeftOp.No_Of_Digits > RightOp.No_Of_Digits )
                    {
                        No_Of_TensComplement_Digits =  LeftOp.No_Of_Digits;
                        flag=0;
                    }
                else if( LeftOp.No_Of_Digits < Integer.No_Of_Digits )
                    {
                        No_Of_TensComplement_Digits =  RightOp.No_Of_Digits;
                        flag=1;
                    }
                else
                    {
                        No_Of_TensComplement_Digits =  LeftOp.No_Of_Digits;

                        for( i=LeftOp.First_NonZero_Digit_Index; i<SIZE; i++)
                            {
                                if( LeftOp.CharInt[i] == RightOp.CharInt[i])
                                    {
                                        continue;
                                    }
                                else if( LeftOp.CharInt[i] > RightOp.CharInt[i])
                                    {
                                        flag=0;
                                        break;
                                    }
                                else if( LeftOp.CharInt[i] < RightOp.CharInt[i])
                                    {
                                        flag=1;
                                        break;
                                    }

                            }

                    }

                if( LeftOp.sign == '+' && RightOp.sign == '-')
                    {
                        RightOp.sign = '+';
                        IntermediateResult = LeftOp+RightOp;

                    }

                else if( LeftOp.sign == '-' && RightOp.sign == '+')
                    {
                        RightOp.sign = '-';
                        IntermediateResult = LeftOp+RightOp;
                    }

                else if( LeftOp.sign == '-' && RightOp.sign == '-')
                    {
                        RightOp.sign = '+';
                        LeftOp.sign = '+';
                        IntermediateResult = RightOp-LeftOp;
                    }

                else if( LeftOp.sign == '+' && RightOp.sign == '+')
                    {
                        if(flag == -1)
                            {
                                for( i=0; i<SIZE; i++)
                                    {
                                        IntermediateResult.CharInt[i]='0';
                                    }
                                IntermediateResult.No_Of_Digits = 1;
                                IntermediateResult.sign = '+';
                                IntermediateResult.First_NonZero_Digit_Index = SIZE-1;
                            }

                        else if(flag == 0 )
                            {
                                for(i=SIZE-1; i >= SIZE - No_Of_TensComplement_Digits; i--)
                                    {
                                        RightOp.CharInt[i] = 105 - RightOp.CharInt[i];
                                        IntermediateResult = LeftOp + RightOp + One;
                                    }
                                if(i >=0)
                                    {
                                        IntermediateResult.CharInt[SIZE-No_Of_TensComplement_Digits-1]='0';
                                    }
                                IntermediateResult.Adjust();
                                IntermediateResult.sign = '+';
                            }

                        else if(flag == 1 )
                            {
                                for(i=SIZE-1; i >= SIZE-No_Of_TensComplement_Digits; i--)
                                    {
                                        LeftOp.CharInt[i] = 105 - LeftOp.CharInt[i];
                                        IntermediateResult = LeftOp + RightOp + One;
                                    }
                                if(i >=0)
                                    {
                                        IntermediateResult.CharInt[SIZE-No_Of_TensComplement_Digits-1]='0';
                                    }
                                IntermediateResult.Adjust();
                                IntermediateResult.sign = '-';
                            }
                    }

                return IntermediateResult;
            }

        BigInteger operator*(BigInteger& Integer)     //  PROPER OVERFLOW CHECK IS REMAINING
            {
                BigInteger IntermediateResult("0"),Temp("0");
                short Multiplicand_Digit,Multiplier_Digit,Result_Digit;
                short carry = 0;
                int i,j,k,shift=0;

                k = SIZE - Integer.No_Of_Digits;

                for( i=SIZE-1; i >= k ; i-- )
                    {
                        Multiplier_Digit = Integer.CharInt[i]-48;

                        for( j=SIZE-1; j>= 0 ; j-- )
                            {
                                Multiplicand_Digit = CharInt[j]-48;
                                Result_Digit =  ( Multiplicand_Digit * Multiplier_Digit + carry )%10;
                                carry = ( Multiplicand_Digit * Multiplier_Digit + carry )/10;
                                Temp.CharInt[j] = Result_Digit + 48 ;
                            }

                        if( carry != 0 )
                            {
                                cout<<"\nOverflow Occured !!!";
                                cout<<"\n";
                                exit(0);
                            }

                        Temp.Adjust();
                        Temp.ShiftLeft(shift);

                        shift++;

                        IntermediateResult = IntermediateResult + Temp;
                        IntermediateResult.Adjust();

                        Temp = "0";
                        carry = 0;
                    }

                IntermediateResult.Adjust();

                if(sign == '+' && Integer.sign == '+')
                {
                    IntermediateResult.sign = '+';
                }
                else if(sign == '-' && Integer.sign == '-')
                {
                    IntermediateResult.sign = '+';
                }
                if(sign == '+' && Integer.sign == '-')
                {
                    IntermediateResult.sign = '-';
                }
                if(sign == '-' && Integer.sign == '+')
                {
                    IntermediateResult.sign = '-';
                }

                return IntermediateResult;
            }

        BigInteger operator^(BigInteger& Integer)
            {
                BigInteger IntermediateResult("1"),One("1"),zero("0");

                while( zero < Integer )
                    {
                        IntermediateResult = IntermediateResult * (*this);
                        zero = zero + One;
                    }
                return  IntermediateResult;

            }

        BigInteger operator/(BigInteger& Integer)
            {
                BigInteger Quotient,Remainder,Dividend,Divisor;

                Dividend = *this;
                Divisor = Integer;



                Divisor.sign = '+';
                Dividend.sign = '+';

                if( Divisor == "1" )
                    {
                        Quotient = *this;

                        if( sign == Integer.sign )
                            {
                                Quotient.sign = '+';

                                return Quotient;
                            }
                        else
                            {
                                Quotient.sign = '-';

                                return Quotient;
                            }
                    }

                else if( Divisor == "0" )
                    {
                        cout<<"\nDivide By Zero Exception !!!\n";
                        exit(0);
                    }
                else if( Divisor > Dividend )
                    {
                        Quotient  = "0";

                        return Quotient;
                    }

                else
                    {
                        BigInteger Result,TempRemainder,One("1"),TempR;
                        int Iteration;

                        Remainder  = Dividend;
                        Quotient = "0";

                        Iteration = Dividend.No_Of_Digits - Divisor.No_Of_Digits + 1;
                        Divisor.ShiftLeft( Dividend.No_Of_Digits - Divisor.No_Of_Digits );

                        while(Iteration > 0 )
                            {
                                if( Divisor <= Remainder )
                                    {
                                            for( Result = "9"; Result > "0"; Result = Result - One)
                                                {
                                                    TempR = Divisor*Result;
                                                    TempRemainder = Remainder - TempR;
                                                        if( TempRemainder >= "0" )
                                                            {
                                                                Remainder = TempRemainder;
                                                                break;
                                                            }
                                                }

                                        Quotient.ShiftLeft(1);
                                        Quotient.CharInt[SIZE-1] = Result.CharInt[SIZE-1];
                                        Divisor.ShiftRight(1);
                                    }
                                else
                                    {
                                        Quotient.ShiftLeft(1);
                                        Divisor.ShiftRight(1);
                                    }

                                Iteration--;
                            }

                    if( sign == Integer.sign )
                    {
                        Quotient.sign = '+';
                    }
                    else
                    {
                        Quotient.sign = '-';
                    }

                    return Quotient;

                    }
            }

        BigInteger operator%(BigInteger& Integer)
            {
                BigInteger Quotient,Remainder,Dividend,Modulus;

                Dividend = *this;
                Modulus = Integer;

                if( Dividend.sign == Modulus.sign )
                    {
                        Quotient.sign = '+';
                    }
                else
                    {
                        Quotient.sign = '-';
                    }


                if( Modulus == "1" )
                    {
                        return "0";
                    }
                else if( Modulus == "0" )
                    {
                        cout<<"\nModulus Can't Be Zero !!!\n";
                        exit(0);
                    }
                else if( Dividend == Modulus )
                    {
                        return "0";
                    }

                else if( Modulus > Dividend )
                    {
                        return Dividend;
                    }
                else
                    {
                        BigInteger Result,TempRemainder,One("1"),TempR;
                        int Iteration;

                        Remainder  = Dividend;
                        Quotient = "0";

                        Iteration = Dividend.No_Of_Digits - Modulus.No_Of_Digits + 1;
                        Modulus.ShiftLeft( Dividend.No_Of_Digits - Modulus.No_Of_Digits );

                        while(Iteration > 0 )
                            {
                                if( Modulus <= Remainder )
                                    {
                                            for( Result = "9"; Result > "0"; Result = Result - One)
                                                {
                                                    TempR = Modulus*Result;
                                                    TempRemainder = Remainder - TempR;
                                                        if( TempRemainder >= "0" )
                                                            {
                                                                Remainder = TempRemainder;
                                                                break;
                                                            }
                                                }

                                        Quotient.ShiftLeft(1);
                                        Quotient.CharInt[SIZE-1] = Result.CharInt[SIZE-1];
                                        Modulus.ShiftRight(1);
                                    }
                                else
                                    {
                                        Quotient.ShiftLeft(1);
                                        Modulus.ShiftRight(1);
                                    }

                                Iteration--;
                            }

                    return Remainder;

                    }
            }

};

        istream& operator>>( istream& Input, BigInteger& Number )
            {
                int Flag = 0, k=0;

                while(Flag == 0)
                {

                Input>>Number.CharInt;

                    if( Number.CharInt[0] == '-')
                        {
                            k=1;
                        }
                    else
                        {
                            k=0;
                        }

                Flag = 1;

                for(int i = k; i<strlen(Number.CharInt); i++)
                    {
                        if(Number.CharInt[i] > 57 || Number.CharInt[i] < 48)
                            {
                                cout<<"\nPlease Provide Numeric Values Only\n";
                                cout<<"Enter Again :\n";
                                Flag = 0;
                                break;
                            }
                    }
                }

                if(Number.CharInt[0] == '-')
                {
                    Number.No_Of_Digits = strlen(Number.CharInt)-1;
                    Number.sign = '-';
                    Number.CharInt[0]='0';
                }
                else
                {
                    Number.No_Of_Digits = strlen(Number.CharInt);
                    Number.sign = '+';
                }

                Number.First_NonZero_Digit_Index = SIZE - Number.No_Of_Digits;
                Number.Align();

                return Input;
            }

        ostream& operator<<( ostream& Output, BigInteger& Number )
            {
                int i;

                if(Number.sign == '-')
                {
                    Output<<"-";
                }

                for( i=Number.First_NonZero_Digit_Index; i<SIZE; i++)
                {
                    Output<<Number.CharInt[i];
                }

                return Output;
            }

        void BigInteger :: NumberOfDigits()
            {
                cout<<No_Of_Digits;
            }

        void BigInteger :: TrailingZeroDisplay() /*Display The Number With Trailing Zeros*/
            {
                int i;

                if(sign == '-')
                {
                    cout<<"-";
                }

                for( i=0; i<SIZE; i++)
                {
                    cout<<CharInt[i];
                }
            }

        void BigInteger :: ShiftLeft( int No_Of_Shifts )
            {
                int Last,i;

                Last = First_NonZero_Digit_Index + No_Of_Digits;


                while( No_Of_Shifts > 0 )
                {

                    if( CharInt[0] == '0')
                        {
                            for( i = First_NonZero_Digit_Index; i < Last; i++ )
                                {
                                    CharInt[i-1] = CharInt[i];
                                }
                                    CharInt[i-1] = '0';
                        }
                    else
                        {
                            cout<<"\nOverflow Occured !!!\n";
                            exit(0);
                        }

                    Last--;
                    First_NonZero_Digit_Index = First_NonZero_Digit_Index - 1;
                    No_Of_Digits = No_Of_Digits + 1;
                    No_Of_Shifts--;

                }
                    Adjust();
            }

        void BigInteger :: ShiftRight( int No_Of_Shifts )
            {
                int i;

                while( No_Of_Shifts > 0 )
                {
                    for( i = SIZE-2; i >= First_NonZero_Digit_Index-1 ; i-- )
                        {
                            CharInt[i+1] = CharInt[i];
                        }

                    First_NonZero_Digit_Index = First_NonZero_Digit_Index + 1;
                    No_Of_Digits = No_Of_Digits - 1;
                    No_Of_Shifts--;
                }

                    Adjust();
            }

//================================Class For Handling Large Integers Ends==================================\\

main()
{
  BigInteger N1,N2,N3;
  short operation;

   cout<<"\t\t"<<SIZE<<" Digit Numbers Arithmetic";
    while(1)
    {
        cout<<"\n\t 1. Add ";
        cout<<"\n\t 2. Subtract ";
        cout<<"\n\t 3. Multiply ";
        cout<<"\n\t 4. Divide ";
        cout<<"\n\t 5. Remainder ";
        cout<<"\n\t 6. Exponentiation ";
        cout<<"\n\t 7. Exit ";
        cout<<"\n\n\t\t Enter The Choice : ";
        cin>>operation;

            switch (operation)
                {
                    case 1 : cout<<"\nEnter First Number :\n";
                             cin>>N1;
                             cout<<"\nEnter Second Number :\n";
                             cin>>N2;
                             N3 = N1+N2;
                             cout<<"\nResult :\n";
                             cout<<N3;
                             break;

                    case 2 : cout<<"\nEnter First Number :\n";
                             cin>>N1;
                             cout<<"\nEnter Second Number :\n";
                             cin>>N2;
                             N3 = N1-N2;
                             cout<<"\nResult :\n";
                             cout<<N3;
                             break;

                    case 3 : cout<<"\nEnter First Number :\n";
                             cin>>N1;
                             cout<<"\nEnter Second Number :\n";
                             cin>>N2;
                             N3 = N1*N2;
                             cout<<"\nProduct :\n";
                             cout<<N3;
                             break;

                    case 4 : cout<<"\nEnter Dividend :\n";
                             cin>>N1;
                             cout<<"\nEnter Divisor :\n";
                             cin>>N2;
                             N3 = N1/N2;
                             cout<<"\nResult :\n";
                             cout<<N3;
                             break;

                    case 5 : cout<<"\nEnter Number :\n";
                             cin>>N1;
                             cout<<"\nEnter Modulus :\n";
                             cin>>N2;
                             N3 = N1%N2;
                             cout<<"\nRemainder :\n";
                             cout<<N3;
                             break;

                    case 6 : cout<<"\nEnter Number :\n";
                             cin>>N1;
                             cout<<"\nEnter Exponent :\n";
                             cin>>N2;
                               while( N2 < "0" )
                                    {
                                        cout<<"\nPlease Provide Positive Exponent!!\n";
                                        cout<<"\nEnter Exponent :\n";
                                        cin>> N2;
                                    }
                             N3 = N1^N2;

                             cout<<"\nResult :\n";
                             cout<<N3;
                             break;
                    case 7 : cout<<"\nThank You For Using\n\n";
                             exit(0);

                    default : cout<<"\n\t Please Enter Appropriate Choice !!";
                             break;
                }
                cout<<"\n";

    };


}
