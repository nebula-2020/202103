/*
 Navicat Premium Data Transfer

 Source Server         : root_connect
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : django_demo

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 25/03/2021 21:20:00
*/
DROP DATABASE IF EXISTS django_demo;

CREATE DATABASE IF NOT EXISTS django_demo DEFAULT CHARACTER SET = utf8mb4 DEFAULT COLLATE = utf8mb4_0900_ai_ci;

USE  django_demo;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `phone` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX phoneUnique(`phone`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for user_details
-- ----------------------------
DROP TABLE IF EXISTS `user_details`;
CREATE TABLE `user_details`  (
  `id` bigint UNSIGNED NOT NULL COMMENT '用户ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户昵称',
  `ps` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '用户个性签名',
  `icon` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '用户头像路径',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for blink
-- ----------------------------
DROP TABLE IF EXISTS `blink`;
CREATE TABLE `blink`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `author_id` bigint UNSIGNED NOT NULL,
  `text` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `like` bigint UNSIGNED NOT NULL DEFAULT 0 COMMENT '点赞量不会实时更新',
  `tags` bigint NOT NULL DEFAULT 0 COMMENT '每一字节代表一个标签，最多8个标签，用户能添加5个，标签总数256个(包括无标签)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
 `permission` bigint NOT NULL AUTO_INCREMENT COMMENT '权限',
 `name` char(8) NOT NULL COMMENT '权限名字最多8个字',
 PRIMARY KEY (`permission`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
 `id` tinyint UNSIGNED NOT NULL COMMENT '角色编号',
 `name` char(8) NOT NULL COMMENT '名字最多8个字',
 `permissions` bigint NOT NULL COMMENT '每一位代表一种权限，某一位为1代表角色具有这种权限',
 PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role_user`;
CREATE TABLE `role_user` (
 `role_id` tinyint UNSIGNED NOT NULL,
 `user_id` bigint UNSIGNED NOT NULL,
 PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

INSERT INTO `permission` (`permission`, `name`) VALUES (b'1','基础权限');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10','读任意用户数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100','写任意用户数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'1000','删任意用户数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10000','读任意文章信息');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100000','写任意文章信息');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'1000000','删任意文章信息');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10000000','读任意话题数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100000000','写任意话题数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'1000000000','删任意话题数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10000000000','读任意举报数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100000000000','写任意举报数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'1000000000000','删任意举报数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10000000000000','增加任意数据');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100000000000000','修改数据表结构');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'1000000000000000','增加数据表');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'10000000000000000','删除数据表');
INSERT INTO `permission` (`permission`, `name`) VALUES (b'100000000000000000','执行任意脚本');

INSERT INTO `role` (`id`, `name`, `permissions`) VALUES (10, '管理员', b'111111111111111111'); -- 啥都能干：管理员
INSERT INTO `role` (`id`, `name`, `permissions`) VALUES (20, '人工审核员', b'000001010000110101'); -- 看文章和封号删文章：人工审核员
INSERT INTO `role` (`id`, `name`, `permissions`) VALUES (30, '数据库维护员', b'011100000000000001'); -- 增删改数据表：数据库维护员
INSERT INTO `role` (`id`, `name`, `permissions`) VALUES (1, '注册用户', b'1'); -- 无特权：注册用户


SET FOREIGN_KEY_CHECKS = 1;
