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

.method public static power(FI)F
Label0:
.var 0 is base F from Label0 to Label1
.var 1 is exp I from Label0 to Label1
Label2:
	iload_1
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	ldc 1.0
	freturn
Label9:
	goto Label5
Label4:
Label5:
	iload_1
	iconst_0
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	ldc 1.0
	fload_0
	iload_1
	ineg
	invokestatic MiniGoClass/power(FI)F
	fdiv
	freturn
Label15:
	goto Label11
Label10:
Label11:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
Label20:
	fload_0
	iload_1
	iconst_2
	idiv
	invokestatic MiniGoClass/power(FI)F
.var 2 is half F from Label20 to Label21
	fstore_2
	fload_2
	fload_2
	fmul
	freturn
Label21:
	goto Label17
Label16:
Label17:
	fload_0
	fload_0
	iload_1
	iconst_1
	isub
	i2f
	invokestatic MiniGoClass/power(FI)F
	fmul
	freturn
Label3:
Label1:
.limit stack 38
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc 2.0
	iconst_3
	invokestatic MiniGoClass/power(FI)F
	invokestatic io/putFloatLn(F)V
	ldc 3.0
	iconst_2
	invokestatic MiniGoClass/power(FI)F
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 2
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
