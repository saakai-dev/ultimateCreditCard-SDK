/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.9
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.doubango.ultimateCreditCard.Sdk;

public class UltCreditCardSdkParallelDeliveryCallback {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  protected UltCreditCardSdkParallelDeliveryCallback(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(UltCreditCardSdkParallelDeliveryCallback obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        ultimateCreditCardSdkJNI.delete_UltCreditCardSdkParallelDeliveryCallback(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  protected void swigDirectorDisconnect() {
    swigCMemOwn = false;
    delete();
  }

  public void swigReleaseOwnership() {
    swigCMemOwn = false;
    ultimateCreditCardSdkJNI.UltCreditCardSdkParallelDeliveryCallback_change_ownership(this, swigCPtr, false);
  }

  public void swigTakeOwnership() {
    swigCMemOwn = true;
    ultimateCreditCardSdkJNI.UltCreditCardSdkParallelDeliveryCallback_change_ownership(this, swigCPtr, true);
  }

  protected UltCreditCardSdkParallelDeliveryCallback() {
    this(ultimateCreditCardSdkJNI.new_UltCreditCardSdkParallelDeliveryCallback(), true);
    ultimateCreditCardSdkJNI.UltCreditCardSdkParallelDeliveryCallback_director_connect(this, swigCPtr, swigCMemOwn, true);
  }

  public void onNewResult(UltCreditCardSdkResult result) {
    ultimateCreditCardSdkJNI.UltCreditCardSdkParallelDeliveryCallback_onNewResult(swigCPtr, this, UltCreditCardSdkResult.getCPtr(result), result);
  }

}
