.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static isLeapYear(I)Id(bool)
Label0:
.var 0 is year I from Label0 to Label1
Label2:
	iload_0
	sipush 400
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_1
	areturn
Label9:
	goto Label5
Label4:
Label5:
	iload_0
	bipush 100
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iconst_0
	areturn
Label15:
	goto Label11
Label10:
Label11:
	iload_0
	iconst_4
	irem
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	areturn
Label3:
Label1:
.limit stack 30
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	sipush 2000
	invokestatic MiniGoClass/isLeapYear(I)Id(bool)
	invokestatic io/putBoolLn(Z)V
	sipush 2020
	invokestatic MiniGoClass/isLeapYear(I)Id(bool)
	invokestatic io/putBoolLn(Z)V
	sipush 2100
	invokestatic MiniGoClass/isLeapYear(I)Id(bool)
	invokestatic io/putBoolLn(Z)V
	sipush 2023
	invokestatic MiniGoClass/isLeapYear(I)Id(bool)
	invokestatic io/putBool(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
