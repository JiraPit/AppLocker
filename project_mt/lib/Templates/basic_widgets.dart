// ignore_for_file: prefer_const_constructors_in_immutables, use_key_in_widget_constructors, prefer_const_constructors
import 'package:rflutter_alert/rflutter_alert.dart';
import 'package:flutter/material.dart';

///Gap
class Gap extends StatelessWidget {
  final double size;
  Gap({required this.size});
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
    );
  }
}

Future<void> showAlert({
  required BuildContext context,
  required AlertType type,
  required String title,
  required String desc,
  required List<List<dynamic>> buttons,
  bool hasClose = false,
  Widget? content,
}) async {
  await Alert(
    style: AlertStyle(
      animationType: AnimationType.fromBottom,
      animationDuration: Duration(milliseconds: 400),
      isOverlayTapDismiss: false,
    ),
    closeIcon: (hasClose)
        ? null
        : SizedBox(
            height: 20,
          ),
    context: context,
    type: type,
    title: title,
    desc: (desc != '') ? desc : null,
    content: content ?? SizedBox(),
    buttons: buttons
        .map(
          (element) => DialogButton(
            child: Text(
              element[0],
              style: TextStyle(
                color: Colors.white,
                fontSize: 20,
              ),
            ),
            onPressed: element[1],
            color: (element.length >= 3) ? element[2] : null,
          ),
        )
        .toList(),
  ).show();
}
