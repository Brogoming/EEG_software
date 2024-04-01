import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


def main():
    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()
    params.serial_port = "COM4"
    board = BoardShim(BoardIds.CYTON_DAISY_BOARD, params)
    board.prepare_session()

    board.start_stream()
    for i in range(10):
        time.sleep(1)
        board.insert_marker(i + 1)
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    print(data)


if __name__ == "__main__":
    main()