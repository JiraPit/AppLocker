// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, override_on_non_overriding_member, non_constant_identifier_names

import 'dart:async';
import 'package:flutter/material.dart';
import 'package:project_mt/Templates/basic_widgets.dart';
import 'package:project_mt/Templates/konstants.dart';
import 'package:rflutter_alert/rflutter_alert.dart';
import 'package:http/http.dart' as http;
import 'package:external_app_launcher/external_app_launcher.dart' as exapp;

class HomeScreen extends StatefulWidget {
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String URL = 'https://dt6fo9.deta.dev/';
  Timer? checker;
  void unlock() {
    showAlert(
      context: context,
      type: AlertType.success,
      title: 'Unlocked',
      desc: '',
      buttons: [],
    );
    Future.delayed(
      Duration(seconds: 2),
      () {
        exapp.LaunchApp.openApp(
          androidPackageName: 'com.spotify.music',
          openStore: true,
        );
      },
    );
  }

  @override
  void initState() {
    super.initState();
    checker = Timer.periodic(Duration(seconds: 2), (t) async {
      http.Response resp = await http.get(
        Uri.parse(URL + 'getstatus'),
      );
      String result = resp.body.toString();
      debugPrint(result);
      if (result == '"false"') {
        unlock();
        checker?.cancel();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        height: double.infinity,
        width: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [kBlue, kPurple],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              margin: EdgeInsets.all(40),
              padding: EdgeInsets.all(50),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(100),
                border: Border.all(width: 15, color: Colors.white),
              ),
              child: Icon(
                Icons.lock,
                color: Colors.white,
                size: 160,
              ),
            ),
            Text(
              'Unlock With RasberryPi',
              style: TextStyle(
                color: Colors.white,
                fontSize: 20,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
