/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.9
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace org.doubango.ultimateCreditCard.Sdk {

using System;
using System.Runtime.InteropServices;

public class UltCreditCardSdkResult : IDisposable {
  private HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal UltCreditCardSdkResult(IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new HandleRef(this, cPtr);
  }

  internal static HandleRef getCPtr(UltCreditCardSdkResult obj) {
    return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
  }

  ~UltCreditCardSdkResult() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          ultimateCreditCardSdkPINVOKE.delete_UltCreditCardSdkResult(swigCPtr);
        }
        swigCPtr = new HandleRef(null, IntPtr.Zero);
      }
      GC.SuppressFinalize(this);
    }
  }

  public UltCreditCardSdkResult(int code, string phrase, string json, uint numCards) : this(ultimateCreditCardSdkPINVOKE.new_UltCreditCardSdkResult__SWIG_0(code, phrase, json, numCards), true) {
  }

  public UltCreditCardSdkResult(int code, string phrase, string json) : this(ultimateCreditCardSdkPINVOKE.new_UltCreditCardSdkResult__SWIG_1(code, phrase, json), true) {
  }

  public int code() {
    int ret = ultimateCreditCardSdkPINVOKE.UltCreditCardSdkResult_code(swigCPtr);
    return ret;
  }

  public string phrase() {
    string ret = ultimateCreditCardSdkPINVOKE.UltCreditCardSdkResult_phrase(swigCPtr);
    return ret;
  }

  public string json() {
    string ret = ultimateCreditCardSdkPINVOKE.UltCreditCardSdkResult_json(swigCPtr);
    return ret;
  }

  public uint numCards() {
    uint ret = ultimateCreditCardSdkPINVOKE.UltCreditCardSdkResult_numCards(swigCPtr);
    return ret;
  }

  public bool isOK() {
    bool ret = ultimateCreditCardSdkPINVOKE.UltCreditCardSdkResult_isOK(swigCPtr);
    return ret;
  }

}

}
