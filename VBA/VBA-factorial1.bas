Attribute VB_Name = "Main"
Sub Factorial()

    Dim Kazu As Long
    Dim Ans As LongLong
    Dim Flag As Byte
    
    Kazu = InputBox("Kazu")
    Ans = 0
    Flag = 0
    
    While Kazu > 1
    
        If Flag = 0 Then
            Ans = Kazu * (Kazu - 1)
            Kazu = Kazu - 1
            Flag = 1
        Else
            Ans = Ans * (Kazu - 1)
            Kazu = Kazu - 1
        End If
        
    Wend
    
    Range("A1") = Ans
    
End Sub
